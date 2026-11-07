# English/Polish loader verification for v0.3

Date: 2026-11-07. Targets: Rise of Mankind — A New Dawn rev1093 and Chronicles of Mankind 1.3.3, using the installed BTS 3.19 executable and the corresponding installed GameCore DLLs.

## Decision

Do not install separate English-only and Polish-only XML files for shared Tags. Do not rely on a ZZZ_ filename to establish precedence. These installations select one language value per record and retain the first registered value for a repeated Tag.

For this release, use a new, independent copy of the selected mod and transform the original Text XML files under their existing names. Preserve every record occurrence and every non-approved language field. Keep the English and Polish exchange XML files outside active Assets directories. Removing the new copy uninstalls the localization without changing the source mod.

This decision follows actual game runs. XML parsing alone did not settle the loading behavior.

## Isolation and evidence

The game was copied in full with cp -a --reflink=auto, without hardlinks. A separate copy of the QA Wine prefix was used. All fixture edits, Python instrumentation, logs, captures, and temporary configuration stayed inside the disposable staging tree, RoM-PL/var/build/english-v03-loader/.

Every run used an unused Xvfb display, separate Xauthority, disabled TCP, and software rendering. The physical desktop and Heroic prefix were not used. Cleanup verifies both the dedicated WINEPREFIX and the per-run GWF_RUN identifier before stopping any remaining Wine process.

The two tested DLL SHA-256 values are:

- AND rev1093: a5a88ede5b0183cc5617c0f672fa74bfb62e7b8d76c7d5b856fed3647759e129
- CoM 1.3.3: 6a6d239dce3d07d6833777976e3a278075833a6d58bcf0d55cd878aba68e19f7

DisableCaching=1 and DisableFileCaching=1 were set in the disposable prefix. The copied cache directory was moved aside before the swapped fixture runs. Fresh logs show actual loads of every fixture and contain no Read GlobalText from cache event.

Machine-readable observations and evidence hashes are in loader-results.json. Each run directory contains results.tsv, init.log, xml.log, PythonErr.log, screen.jpg, and the launcher log.

## Minimal experiment

Three files contain overlapping artificial Tags:

- AAA_GWF_PROBE_BASE.xml: complete English and Polish baseline records.
- ZZZ_A_GWF_PROBE.xml: English-only, Polish-only, combined, empty-Polish, repeated-Tag, and grammatical-form records.
- ZZZ_B_GWF_PROBE.xml: the same split-language Tags in the opposite language.

The first variant creates these files in reverse filename order. The second recreates them in forward filename order and swaps the A/B contents. Saved fixture files and SHA manifests make both arrangements repeatable. A Python hook in the copied mod calls the game's actual CyTranslator after initialization and records the returned strings.

Fixture generation: var/tools/english_v03_loader_fixture.py. Isolated runner: var/tools/english_v03_loader_qa.sh. The original generic Xvfb QA script was reused as the runner's basis.

Select the copied mod and language in the disposable CivilizationIV.ini, then run:

~~~sh
GWF_RUN=rom-probe-repeat GWF_MOD='Rise of Mankind - A New Dawn' GWF_LANGUAGE=English GWF_PROBE_OUTPUT='Z:/home/zazpany/Dane/Projekty/RoM-PL/var/reports/english-v03-loader/rom-probe-repeat/results.tsv' bash /home/zazpany/Dane/Projekty/RoM-PL/var/tools/english_v03_loader_qa.sh --game
~~~

Use a fresh run name and the disposable game/prefix only.

## Observed behavior

| Question | Observed result |
| --- | --- |
| Are English and Polish records with the same Tag merged? | No. Only the chosen text of each record reaches the translation manager. |
| English-only record while Polish is selected | Its English value can become the active Polish-language result via fallback. |
| Polish-only record while English is selected | Its Polish value can become the active English-language result via the first-field fallback. |
| Empty Polish with nonempty English | English is selected by fallback. |
| Repeated Tag in a single file | The first record wins; subsequent records do not replace it. |
| Repeated Tag in separate files | The first loaded definition wins in the tested binaries. |
| Are filenames loaded lexicographically? | No. Both complete logs show nonalphabetical ordering. |
| Are the two mods' orders identical? | No, despite identical fixture filenames and contents. |
| Do nested Text values and grammatical forms load? | Yes. Colon-separated forms were returned through getObjectText(key, 0/1) in the fixture. |
| Does Modules provide a reliable overriding layer here? | No. The tested module loaded after Text and did not override existing Tags. |

The fixture subsequence in AND was A → baseline → B. In CoM it was B → baseline → A. Swapping A/B contents changed the winning value, while reversing physical creation order did not produce alphabetical loading.

A module file at Assets/Modules/GreywolfLoaderProbe/GWF_CIV4GameText.xml was also tested. Unique module-only Tags were returned, proving that the module loaded. Tags already registered from Text retained their Text values. This is direct evidence against using that module as an override in these deployed binaries.

The inspected AND/CoM CvGameText source explains named-language selection, fallback to English, and fallback to the first language field. The referenced CoM LoadGlobalText source prepends a module vector, whereas the installed binaries loaded the probe module after Text. That source was therefore not accepted as proof of deployed precedence.

## Candidate installation checks

Independent copies named Rise of Mankind - A New Dawn - Greywolf Forge and Chronicles of Mankind - Greywolf Forge both loaded successfully with matching mod INI filenames. The exact first installer outputs (44/58 original XML filenames, no additional ZZZ file) were tested in English and Polish. All four starts produced fresh matching language/mod logs and empty PythonErr.log files.

The initial input/output file hashes are recorded in candidate-initial-files.json. These runs validate that candidate only; the final release requires reruns against its final frozen files.

## Runtime export coverage and limits

Full menu-safe text was exported using CyTranslator.getText:

| Target | Distinct exported keys | Successful values | Known pre-existing exception | Excluded context-dependent/potentially formatted keys |
| --- | ---: | ---: | ---: | ---: |
| AND | 13,904 | 13,903 | 1 | 4,156 |
| CoM | 18,251 | 18,250 | 1 | 4,247 |

The common exception is CHANGED_TXT_KEY_UNIT_TRIREME_PEDIA, which returned an unidentifiable C++ exception in both baseline and candidate. Dynamic diplomacy placeholders such as [CT_NAME] and [OUR_CIV_SHORT] require an active game context and cannot be evaluated safely at the main menu. The conservative menu filter also excludes potentially formatted text. It is documented in dump-keysets-filtered.json; excluded texts are not claimed as runtime-tested.

These samples complement structural comparison of every published Polish field, duplicate occurrence, placeholder, grammatical metadata, and non-approved field. They do not replace it.

In the initial English comparison, AND changed only two exported keys, both approved corrections. CoM changed three approved keys plus eleven accent-decoding results when pinned ISO-8859-1 inputs were normalized to UTF-8. Examples include Abb?ierre becoming Abbé Pierre. Complete before/after values are retained in the corresponding initial-English diff JSON files.

## Polish glyph probe

A temporary marker containing ąćęłńóśźż ĄĆĘŁŃÓŚŹŻ replaced one menu label only in the disposable AND copy. The captured menu showed the Polish glyphs, including ę/ń. The original INTERFACE.xml was restored byte for byte and its before/after hashes were compared.

The initial run used the previously installed Sylfaen CIV4 theme/font. That custom family is registered from the host user's font directory; pristine AND/CoM mods ship a different family, Sylfaen. The initial glyph run alone therefore did not prove that a pristine theme works.

A separate experiment replaced only the disposable copy's theme with the exact preserved original theme (SHA-256 045c154b2140778dcca865a23ccca7c6b266ebb92d7a5ebc1418f6c07ce16a9c), retained native Unicode Polish, and repeated the alphabet marker. It rendered correctly, including ę/ń and capital variants. WINEDEBUG=trace+font established the actual selection: requests for Sylfaen resolved to Arial / Arial Bold from the isolated prefix's Windows Fonts directory. They did not select Sylfaen CIV4. Thus the previous custom font patch is not required for this tested original-theme configuration; this is an Arial fallback result, not a test of actual original Sylfaen rendering.

The verified environment is LANG=pl_PL.UTF-8, LC_ALL=pl_PL.UTF-8, Wine LocaleName=pl-PL, Locale=00000415, ACP=1250, OEMCP=852, MACCP=10029, and game language Polish=7. The original-theme files and temporary marker XML were restored byte for byte after each run. The installer itself preserves the source theme and fonts. The result does not certify arbitrary Wine code pages or native Windows.

An earlier strace attempt obtained a completed text dump but captured the initialization screen due to tracing overhead. That attempt is retained as startup evidence and is not a glyph PASS.

Evidence: font-provenance.json, rom-glyphs/glyph-crop.jpg, rom-original-font-glyphs-visible/glyph-crop.jpg, rom-original-font-selection/selected-faces.log, and the fixture manifests in those run directories.

## Final frozen release acceptance

The actual frozen portable install.py (SHA-256 319abfc950fd7baaf60ba441340989cfc1309c03033be91d83d16ad8cf922e42) was executed against both original source mods, creating fresh disposable copies with the Greywolf Forge suffix. Earlier test copies were moved outside the staged Mods directory first. The installed 44/58 XML files matched every frozen output hash. Query-only Python hooks were then added to those disposable copies; XML and DLL files remained unchanged.

All four real-game runs passed:

| Run | Language | Exported distinct keys | Successful values | Corrected catalogue Tags returned | PythonErr bytes |
| --- | --- | ---: | ---: | ---: | ---: |
| AND | English 0 | 13,919 | 13,918 | 18/18 | 0 |
| AND | Polish 7 | 13,919 | 13,918 | 18/18 | 0 |
| CoM | English 0 | 18,266 | 18,265 | 18/18 | 0 |
| CoM | Polish 7 | 18,266 | 18,265 | 18/18 | 0 |

The single exception in each broad dump is the same historical CHANGED_TXT_KEY_UNIT_TRIREME_PEDIA query described above. None of the 18 corrected catalogue Tags failed. All long articles were returned, including the approximately 141,000-character English Unique Buildings article. Literal text segments of at least three characters were checked against the exact frozen source fields after normalizing the engine's CP1250 byte-valued characters and HTML entities. Parameterized event text was queried with explicit synthetic string/numeric arguments. Ordinary bracketed prose (including the AI-only war-weariness qualifier) stays in these literal comparisons. Every English record also has an explicit characteristic fragment from an approved replacement confirmed in the returned value; every Polish expected field is independently matched to the published v0.2 XML. Full original returned representations, hashes, argument types, and checks remain in the report; these checks do not claim pixel-level layout review of every article.

The shared broad Polish samples (13,904 AND / 18,251 CoM keys) are unchanged from the earlier native-v0.2 Polish candidate. Against the original English baseline, AND has three approved changed keys; CoM has three approved changed keys plus the same eleven known ISO-8859-1-to-UTF-8 accent-decoding changes. There are no unexpected differences in these shared samples. The additional fifteen final keys per mod cover the remainder of the eighteen-entry catalogue that the broad menu-safe filter had excluded.

Both cache flags remained disabled, and each copied cache directory was moved aside before its run. Fresh logs show all frozen Text files loaded. Every screenshot was visually inspected and shows the expected mod and language at the rendered main menu. The four final copied mods retain the source's existing theme; the separate original-theme/Arial fallback proof is documented above.

Final output-set SHA-256 values:

- RoM-PL: 34a31e938baa1cea08c5e71442fc4bda86fe0fccaa41b20e5fe4f496f0cee626
- CoM-PL: 867f0f681eb0221eb9520f5a30e53e486927785838eb951d234c57cf97d6ae25

Final catalogue SHA-256 values:

- RoM-PL: da6a04af05cc6489dbc26a71f1508f1332f7e9570b9490fbae1c99fe71fbb22b
- CoM-PL: e90c2af4fa1a87bab60512a656d1bdb7ad4639ecd8f1e24469e11b623c42016a

The original installed source Text files, DLLs, and themes remain byte-identical after all probes: 46/46 AND and 60/60 CoM verified files. No native Windows, map, turn progression, or save/load compatibility claim is made.

Machine-readable final gate: final-release-qa.json. Full returned catalogue values: final-catalogue-lookups.json. Fresh-install evidence: final-install.json. Four-menu visual evidence: final-menu-contact-sheet.jpg. Independent installer findings and fixes: installer-review.json.
