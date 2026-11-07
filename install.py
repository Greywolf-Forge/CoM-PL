#!/usr/bin/env python3
"""Install a verified Greywolf Forge localization into a NEW copy of a mod.

Python 3.10+, standard library only. The source mod is never written to.
Uninstall by removing the created copy; the source remains usable throughout.
"""
from pathlib import Path
from collections import Counter, defaultdict
from hashlib import sha256
from xml.etree import ElementTree as E
from xml.sax.saxutils import escape
import argparse, json, re, shutil, sys

TEXT = re.compile(r'<TEXT(?:\s[^>]*)?>.*?</TEXT>', re.S)
COMMENT = re.compile(r'<!--.*?-->', re.S)
PL = re.compile(r'<Polish\b[^>]*?(?:/>|>.*?</Polish>)', re.S)
EN = re.compile(r'<English(?:\s[^>]*)?>(.*?)</English>', re.S)
# Civ control names are uppercase; prose notes such as [-1 above Noble]
# are ordinary text. Preserve links, colour arguments and printf parameters.
TOKEN = re.compile(r'\[[\\/]?[A-Z][A-Z0-9_]*(?:[=:][^\[\]\r\n]*)?\]|%%|%[A-Za-z]\d*(?::\d+)?(?:_[A-Za-z0-9_]+)?')
FORMAT_TOKENS = {'[NEWLINE]','[BOLD]','[\\BOLD]'}
LOCAL = lambda node: node.tag.rsplit('}',1)[-1]

def sha(blob):
    return sha256(blob).hexdigest()

def tokens_sha(tokens):
    return sha(json.dumps(tokens,ensure_ascii=False,separators=(',',':')).encode())

def check_tokens(old,new,approval=None):
    before,after=TOKEN.findall(old),TOKEN.findall(new)
    if before==after:return
    if not approval or not approval.get('reason'):
        raise ValueError('Runtime tokens differ')
    if tokens_sha(before)!=approval.get('original_tokens_sha256') or tokens_sha(after)!=approval.get('corrected_tokens_sha256'):
        raise ValueError('Unapproved formatting tokens')
    if [t for t in before if t not in FORMAT_TOKENS]!=[t for t in after if t not in FORMAT_TOKENS]:
        raise ValueError('Protected runtime tokens differ')

def active_matches(pattern, text):
    """Match active XML only; spaces preserve offsets into the original text."""
    masked = COMMENT.sub(lambda m: ' ' * len(m.group()), text)
    return list(pattern.finditer(masked))

def replace_spans(text, spans):
    pieces=[]; cursor=0
    for a,b,replacement in sorted(spans):
        if a<cursor:raise ValueError('Overlapping replacements')
        pieces.extend((text[cursor:a],replacement));cursor=b
    pieces.append(text[cursor:])
    return ''.join(pieces)

def protected_xml(text):
    spans = [(m.start(), m.end(), '') for m in active_matches(PL, text)]
    spans += [(m.start(), m.end(), '<English/>') for m in active_matches(EN, text)]
    return replace_spans(text,spans)

def normalize(raw, filename):
    header = re.search(rb'<\?xml[^>]*encoding=["\']([^"\']+)["\']',raw[:256],re.I)
    encoding = header.group(1).decode('ascii') if header else 'utf-8'
    text = raw.decode(encoding).lstrip('\ufeff \t\r\n')
    text = re.sub(r'(<\?xml[^>]*encoding=["\'])([^"\']+)',lambda m:m.group(1)+'UTF-8',text,count=1,flags=re.I)
    # The pinned CoM source has one known unescaped ampersand in this file.
    # No arbitrary repair is attempted for unrecognized source hashes/files.
    if filename == 'Chronicles_Buildings.xml':
        text = re.sub(r'&(?!#\d+;|#x[0-9a-fA-F]+;|amp;|lt;|gt;|quot;|apos;)', '&amp;',text)
    E.fromstring(text.encode('utf-8'))
    return text

def scan(text):
    masked = COMMENT.sub(lambda m:' '*len(m.group()),text)
    counts = Counter()
    for match in TEXT.finditer(masked):
        raw=text[match.start():match.end()]
        node=E.fromstring(raw)
        tag=next(c.text for c in node if LOCAL(c)=='Tag')
        occurrence=counts[tag]
        counts[tag]+=1
        yield (tag,occurrence),node,raw,match.start(),match.end()

def polish_fields(blob):
    result={}
    for (tag,occ),_,raw,_,_ in scan(blob.decode('utf-8')):
        if occ:raise ValueError('Duplicate published Polish Tag: '+tag)
        result[tag]=[raw[m.start():m.end()] for m in active_matches(PL,raw)]
        if not result[tag]:raise ValueError('Missing Polish: '+tag)
    return result

def transform(text,polish,edits):
    """Change only approved English and exactly published v0.2 Polish fields."""
    spans=[];seen=set()
    for key,node,raw,offset,_ in scan(text):
        tag,occ=key
        if tag in polish:
            fields=active_matches(PL,raw)
            replacement=''.join(polish[tag])
            if fields:
                for i,f in enumerate(fields):
                    spans.append((offset+f.start(),offset+f.end(),replacement if i==0 else ''))
            else:
                at=offset+raw.rindex('</TEXT>');spans.append((at,at,replacement))
        if key not in edits:continue
        record=edits[key]
        fields=[n for n in node if LOCAL(n)=='English']
        if len(fields)!=1 or len(fields[0]):raise ValueError('Unsupported English structure: '+tag)
        old=fields[0].text or ''
        if sha(old.encode())!=record['original_english_sha256']:raise ValueError('English source differs: '+tag)
        new=old
        for r in record['replacements']:
            if not r['old'] or new.count(r['old'])!=r.get('expected_count',1):raise ValueError('Ambiguous correction: '+tag)
            new=new.replace(r['old'],r['new'])
        if sha(new.encode())!=record['corrected_english_sha256']:raise ValueError('English result differs: '+tag)
        check_tokens(old,new,record.get('formatting_token_exception'))
        f=active_matches(EN,raw)
        if len(f)!=1:raise ValueError('Ambiguous English field: '+tag)
        spans.append((offset+f[0].start(1),offset+f[0].end(1),escape(new)))
        seen.add(key)
    if set(edits)!=seen:raise ValueError('Missing English correction targets')
    output=replace_spans(text,spans)
    if protected_xml(text)!=protected_xml(output):raise ValueError('Unapproved XML bytes changed')
    if COMMENT.findall(text)!=COMMENT.findall(output):raise ValueError('XML comments changed')
    E.fromstring(output.encode('utf-8'))
    return output.encode('utf-8')

def prepare(package,source):
    manifest=json.loads((package/'manifest.json').read_text(encoding='utf-8'))
    install=manifest['installation']
    for relative,want in install.get('source_guard_files',{}).items():
        path=source/relative
        if not path.is_file() or sha(path.read_bytes())!=want:
            raise ValueError('Unsupported source binary/data checksum: '+relative)
    catalog_bytes=(package/'patches/english-corrections-v0.3.json').read_bytes()
    if sha(catalog_bytes)!=install['catalogue_sha256']:raise ValueError('Correction catalogue checksum differs')
    catalog=json.loads(catalog_bytes)
    polish_bytes=(package/'upstream/ZZZ_GreywolfForge_Polish.xml').read_bytes()
    if sha(polish_bytes)!=catalog['base_polish_sha256']:raise ValueError('Published Polish checksum differs')
    polish=polish_fields(polish_bytes)
    byfile=defaultdict(dict)
    for r in catalog['records']:
        key=(r['tag'],r['occurrence'])
        if key in byfile[r['source_file']]:raise ValueError('Duplicate catalogue target')
        byfile[r['source_file']][key]=r
    directory=source/'Assets/XML/Text'
    if not directory.is_dir():raise ValueError('Select the mod directory containing Assets/XML/Text')
    actual={p.name for p in directory.iterdir() if p.is_file() and p.suffix.lower()=='.xml'}
    expected=set(install['source_files'])
    legacy='ZZZ_GreywolfForge_Polish.xml'
    removable=[]
    if legacy in actual and sha((directory/legacy).read_bytes())==catalog['base_polish_sha256']:
        actual.remove(legacy);removable.append(legacy)
    if actual!=expected:raise ValueError('Source XML set differs; missing='+str(sorted(expected-actual))+' extra='+str(sorted(actual-expected)))
    output={};sources={}
    for filename,info in install['source_files'].items():
        raw=(directory/filename).read_bytes()
        if sha(raw) not in info['accepted_sha256']:raise ValueError('Unsupported source checksum: '+filename)
        sources[filename]=sha(raw)
        text=normalize(raw,filename)
        output[filename]=transform(text,polish,byfile[filename])
    if set(byfile)-expected:raise ValueError('Unknown catalogue source file')
    return manifest,output,removable,sources

def install(package,source,destination,check=False):
    source=source.resolve(strict=True)
    destination=destination.absolute()
    if destination.exists() or destination.is_symlink():raise ValueError('Destination must be a NEW directory')
    resolved=destination.resolve()
    if source==resolved or source in resolved.parents or resolved in source.parents:
        raise ValueError('Source and destination must be separate sibling trees')
    manifest,output,removable,sources=prepare(package,source)
    if check:
        return {'status':'VALIDATED_NO_FILES_WRITTEN','files':len(output),'destination':str(destination)}
    # copytree without symlinks/hardlinks makes all edited files independent.
    # Existing directories are rejected, including an incomplete earlier run.
    shutil.copytree(source,destination,symlinks=False)
    target=destination/'Assets/XML/Text'
    for filename,blob in output.items():
        (target/filename).write_bytes(blob)
    for filename in removable:(target/filename).unlink()
    original_ini=destination/(source.name+'.ini')
    new_ini=destination/(destination.name+'.ini')
    if original_ini.is_file() and not new_ini.exists():shutil.copy2(original_ini,new_ini)
    # Prove the source has remained unchanged while creating the copy.
    for filename,want in sources.items():
        if sha((source/'Assets/XML/Text'/filename).read_bytes())!=want:raise ValueError('Source changed concurrently: '+filename)
    for relative,want in manifest['installation'].get('source_guard_files',{}).items():
        if sha((source/relative).read_bytes())!=want:raise ValueError('Source changed concurrently: '+relative)
    marker={'project':manifest['project'],'release':manifest['release'],'source':str(source),'files':{name:sha(blob) for name,blob in output.items()},'uninstall':'Remove only this copied mod directory. The source mod was not modified.'}
    (destination/'GREYWOLF_LOCALIZATION.json').write_text(json.dumps(marker,indent=2)+'\n',encoding='utf-8')
    return {'status':'INSTALLED_COPY','files':len(output),'destination':str(destination),'source_unchanged':True}

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--source',type=Path,required=True,help='Existing supported mod folder')
    p.add_argument('--destination',type=Path,required=True,help='New mod folder next to the original')
    p.add_argument('--check',action='store_true',help='Validate without copying or writing')
    args=p.parse_args()
    try:
        result=install(Path(__file__).resolve().parent,args.source,args.destination,args.check)
    except (OSError,ValueError,E.ParseError,KeyError) as e:
        print('Installation stopped: '+str(e),file=sys.stderr)
        return 1
    print(json.dumps(result,indent=2))
    return 0

if __name__=='__main__':sys.exit(main())
