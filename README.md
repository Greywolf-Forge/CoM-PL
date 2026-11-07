# CoM-PL

Polish localization and verified English source corrections for **Chronicles of Mankind 1.3.3**, Civilization IV: Beyond the Sword 3.19.

**v0.3 candidate — not published as a stable release.** The stable [v0.2 release](https://github.com/Greywolf-Forge/CoM-PL/releases/tag/v0.2) is unchanged.

[English](#english) | [Polski](#polski)

## English

The candidate adds source-verified English corrections while retaining the complete published v0.2 Polish text. See [UPSTREAM_CORRECTIONS.md](UPSTREAM_CORRECTIONS.md) for the exact changes, evidence and historical version notes.

### Installation into a separate mod copy

Requires Python 3.10 or newer, the supported mod version, and free space for another copy of that mod. Close the game first.

Run this from the extracted package, replacing the paths with your installation:

```sh
python3 install.py --source "/path/to/Beyond the Sword/Mods/Chronicles of Mankind" --destination "/path/to/Beyond the Sword/Mods/Chronicles of Mankind - Greywolf Forge"
```

On Windows use `py -3 install.py` with the same arguments. Add `--check` to validate the source without creating files. The destination must not exist. In Beyond the Sword, load **Chronicles of Mankind - Greywolf Forge**, then select English or Polish.

The installer validates source hashes and creates an independent copy. It changes only text files in the copy and creates a matching mod configuration filename. Your original mod remains available. To uninstall, delete only the newly created copy.

**Do not place the files from `upstream/` into XML/Text together.** Current DLL tests show that duplicate Tags do not merge language fields and that alphabetical filename order does not guarantee priority. These files are for maintainers to merge; the installer avoids that collision.

### For mod authors

[UPSTREAM_CORRECTIONS.md](UPSTREAM_CORRECTIONS.md) contains each confirmed correction and its evidence. [The patch catalogue](patches/english-corrections-v0.3.json) is the single source used for generation. The English exchange XML contains complete corrected English entries; the Polish exchange XML retains the exact v0.2 translation and grammar.

Original source text and previous translations retain their authors' rights. Greywolf Forge's own corrections and tooling are covered by [LICENSE](LICENSE).

### Candidate verification

19 new automated tests pass, covering original source hashes, exact Polish preservation, record occurrences, placeholders, grammar, other languages, reproducible generation, isolated installation and removal. Final game/font QA and the broader v0.2 regression gate are still pending. Native Windows has not been tested.

## Polski

Kandydat v0.3 dodaje zweryfikowane poprawki angielskich źródeł i zachowuje dokładną treść polskiego wydania v0.2. Lista zmian z dowodami znajduje się w [UPSTREAM_CORRECTIONS.md](UPSTREAM_CORRECTIONS.md).

### Instalacja

Potrzebujesz Python 3.10 lub nowszego, wskazanej wersji moda i miejsca na jego dodatkową kopię. Zamknij grę. Uruchom polecenie z sekcji angielskiej, wpisując ścieżkę istniejącego moda i **nowy, nieistniejący folder** obok niego. Na Windows użyj `py -3`, na Linuxie `python3`. Opcja `--check` sprawdza zgodność bez zapisywania plików.

W grze wybierz **Chronicles of Mankind - Greywolf Forge**, następnie język Polski lub English. Instalator pracuje w osobnej kopii; oryginalnego moda nie zmienia. Odinstalowanie polega na usunięciu utworzonej kopii.

Pliki `ZZZ` z katalogu `upstream/` służą autorom do scalania. **Nie kopiuj ich razem do XML/Text.** Testy aktualnych DLL wykazały kolizje języków i brak gwarancji kolejności wynikającej z nazwy pliku.

Kandydat przeszedł 19 nowych testów. Końcowa weryfikacja w grze, kontrola czcionek i pełna regresja v0.2 są jeszcze w toku. Wydanie stabilne v0.3 nie zostało opublikowane.
