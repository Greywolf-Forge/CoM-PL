# CoM-PL

Polish localization and verified English source corrections for **Chronicles of Mankind 1.3.3**, Civilization IV: Beyond the Sword 3.19.

**[Download v0.3](https://github.com/Greywolf-Forge/CoM-PL/releases/tag/v0.3)** · [Corrections for mod authors](UPSTREAM_CORRECTIONS.md) · [Loader and QA](docs/LOADER-v0.3.md)

[English](#english) | [Polski](#polski)

## English

v0.3 contains **123 confirmed correction groups in 18 English entries**, comprising 187 exact replacement rules and 201 affected literal occurrences. The published **v0.2 Polish translation is preserved byte for byte**, including grammatical forms. The audit read 16 short English entries and seven complete articles; two additional articles were checked in selected passages. Six optional editorial suggestions remain outside the release.

The changes cover source-backed mechanics, arithmetic, factual and language errors. Historical guides retain their author voice and version-specific examples. [UPSTREAM_CORRECTIONS.md](UPSTREAM_CORRECTIONS.md) gives the original and corrected fragments, source hashes, evidence and compatibility notes for every group.

### Install a separate mod copy

Requirements: **Python 3.10+**, the supported mod and DLL revision, and space for an independent copy of the mod. Close the game. Extract the release ZIP and run the following command from its directory, substituting your paths:

```sh
python3 install.py --source "/path/to/Beyond the Sword/Mods/Chronicles of Mankind" --destination "/path/to/Beyond the Sword/Mods/Chronicles of Mankind - Greywolf Forge"
```

On Windows use `py -3 install.py` with the same arguments. Add `--check` to validate without creating files. **The destination must be a new directory**, normally beside the original mod under `Mods`. Load **Chronicles of Mankind - Greywolf Forge** in Beyond the Sword and choose English or Polish.

The installer validates the source Text XML and GameCore DLL hashes, copies the complete mod, and updates 58 Text XML files under their existing names. It also creates the matching mod INI filename. Source files remain unchanged. A recognized v0.2 ZZZ overlay is removed only from the new copy; an unknown overlay or unsupported revision stops validation before copying. To uninstall, remove only the created mod copy.

**Wine:** the verified configuration uses the Polish Windows locale (`pl-PL`, `0415`) and code page **1250**, with `LANG=pl_PL.UTF-8` and `LC_ALL=pl_PL.UTF-8`. Selecting Polish in the game does not by itself establish the prefix's Windows locale. The installer does not configure Wine. The original Sylfaen theme rendered Polish correctly through the tested runner's Arial/Arial Bold fallback; the earlier custom Sylfaen CIV4 patch is not required for that verified configuration. See [font provenance and exact QA conditions](docs/QA-v0.3.json).

### Exchange XML files

The two XML files in `upstream/` are for maintainers to merge using the catalogue's source file, Tag and occurrence. **Do not install them together as runtime overlays.** Actual game tests show that duplicate Tags select the first loaded value, do not merge language fields, and are not ordered reliably by an alphabetical filename prefix. The installer uses the original source filenames in a separate copy instead.

The English exchange XML contains complete corrected entries. The Polish exchange XML is exactly the published v0.2 file. The [canonical patch catalogue](patches/english-corrections-v0.3.json) generates both the corrections and their documentation.

### Verification and limits

**70/70 automated tests pass:** 24 English/installer checks and 46 regression checks against the immutable v0.2 baseline. Both final mod copies were installed using the distributed installer and loaded in English and Polish on isolated Wine/Xvfb. Fresh logs, empty PythonErr files, text exports, font inspection and frozen XML hashes are recorded in [QA-v0.3.json](docs/QA-v0.3.json).

This verifies the pinned versions and documented Wine configuration. Native Windows, arbitrary Wine code pages, full campaigns, turn progression and save/load were not tested for this revision. The targeted English audit does not claim to proofread every source entry. Deferred and rejected findings are listed in the upstream document.

The original mod text and earlier translations remain the work of their respective authors. Greywolf Forge's own changes and tooling are covered by [LICENSE](LICENSE). The package contains no game binaries or font files. The [v0.2 release](https://github.com/Greywolf-Forge/CoM-PL/releases/tag/v0.2) and its assets remain unchanged.

## Polski

v0.3 dodaje **123 grupy potwierdzonych korekt w 18 wpisach English**: 187 reguł zamiany i 201 poprawianych wystąpień. **Polish pozostaje bajt w bajt zgodny z wydaniem v0.2**, łącznie z odmianą i metadanymi gramatycznymi. Przegląd objął 25 angielskich wpisów: 16 krótkich i siedem artykułów przeczytanych w całości oraz dwa artykuły sprawdzone fragmentami. Sześć sugestii redakcyjnych odłożono.

### Instalacja

Potrzebujesz Python 3.10 lub nowszego, zgodnej wersji moda i miejsca na jego dodatkową kopię. Zamknij grę. Uruchom polecenie z sekcji angielskiej, podając istniejący katalog źródłowy i **nowy, nieistniejący katalog obok niego**. Na Windows użyj `py -3`, na Linuxie `python3`. Opcja `--check` sprawdza źródło bez zapisywania plików.

W grze wybierz **Chronicles of Mankind - Greywolf Forge**, następnie język Polski lub English. Oryginalny mod pozostaje nietknięty. Odinstalowanie polega na usunięciu utworzonej kopii.

Pod Wine sprawdzono polskie ustawienia Windows (`pl-PL`, strona kodowa 1250) oraz poprawny font z polskimi glifami. Sama zmiana języka w grze nie ustawia strony kodowej prefiksu. Instalator nie zmienia prefiksu Wine, motywu ani fontów. Oryginalny motyw poprawnie renderował alfabet przez zastępczy Arial; natywnego Windows nie testowano.

Pliki `ZZZ` w `upstream/` służą autorom do przenoszenia zmian. **Nie kopiuj ich razem do XML/Text**: rzeczywisty loader nie scala języków powtarzającego się Tag i nie gwarantuje priorytetu wynikającego z nazwy pliku.

Wynik: **70/70 testów automatycznych PASS**, końcowa instalacja pełnej kopii oraz uruchomienia obu języków na izolowanym Xvfb. [Pełna lista poprawek z dowodami](UPSTREAM_CORRECTIONS.md) i [raport QA](docs/QA-v0.3.json) opisują zakres oraz ograniczenia.
