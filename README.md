# CoM-PL

Polish translation of Chronicles of Mankind 1.3.3 for Civilization IV: Beyond the Sword 3.19.

Polskie tłumaczenie Chronicles of Mankind 1.3.3 do Civilization IV: Beyond the Sword 3.19.

[English](#english) | [Polski](#polski)

## English

Current translation: **0.2**. [Download the release](https://github.com/Greywolf-Forge/CoM-PL/releases/tag/v0.2) or see the [changes](CHANGELOG.md).

The full editorial review is complete. Version 0.2 corrects **9,973 entries** compared with 0.1.1.

### Install

1. You need Beyond the Sword 3.19 and Chronicles of Mankind 1.3.3.
2. Download [`ZZZ_GreywolfForge_Polish.xml`](https://github.com/Greywolf-Forge/CoM-PL/releases/download/v0.2/ZZZ_GreywolfForge_Polish.xml).
3. Put it in:

   ```
   Beyond the Sword/Mods/Chronicles of Mankind/Assets/XML/Text/
   ```

4. In the game options set the language to Polish. Leave the font settings as they are (Sylfaen).

Alternatively, download [CoM-PL-v0.2.zip](https://github.com/Greywolf-Forge/CoM-PL/releases/download/v0.2/CoM-PL-v0.2.zip), extract it into a separate directory, and copy only its `Assets` directory into the mod directory. When updating, replace the previous `ZZZ_GreywolfForge_Polish.xml` with this version.

To uninstall, delete that one file. Nothing else in the mod is changed.

### For mod authors

The file has 17 832 entries with Tag and Polish only, including the grammar fields Civ4 needs. No English, no other languages, no gameplay data. You can ship it as a separate XML or merge the Polish fields by Tag. If your mod version differs, check for key collisions first.

[`manifest.json`](manifest.json) lists the source mod version, entry count, SHA-256 and resolved conflicts.

### License

Greywolf Forge translations and fixes are MIT licensed, see [LICENSE](LICENSE). Use them in your mod and change them as you like, no need to ask. Some texts come from earlier translators of the mod. They are not covered by this license and their rights stay with them.

### Testing

Version 0.2 passed all **46 static and integration tests**, covering XML structure, keys, parameters, numbers, encoding and file hashes. All documented numeric and runtime-token differences are resolved. The overlay format was previously tested in Wine/Xvfb with a Polish locale. This revision has not been tested in a running game or on native Windows 10/11. If you see missing text or broken Polish characters (ę, ń), [open an issue](https://github.com/Greywolf-Forge/CoM-PL/issues/new/choose). You can also reach us on [Discord](https://discord.gg/TYcdct6fTn).

Only 1.3.3 is supported. Other versions may not match.

Unofficial fan translation. Original mod: https://forums.civfanatics.com/forums/civ4-chronicles-of-mankind.628/

## Polski

Wersja tłumaczenia: **0.2**. [Pobierz wydanie](https://github.com/Greywolf-Forge/CoM-PL/releases/tag/v0.2) lub zobacz [listę zmian](CHANGELOG.md).

Pełna korekta redakcyjna jest zakończona. Wersja 0.2 obejmuje poprawki w **9 973 wpisach** względem 0.1.1.

### Instalacja

1. Potrzebujesz Beyond the Sword 3.19 i Chronicles of Mankind 1.3.3.
2. Pobierz plik [`ZZZ_GreywolfForge_Polish.xml`](https://github.com/Greywolf-Forge/CoM-PL/releases/download/v0.2/ZZZ_GreywolfForge_Polish.xml).
3. Skopiuj go do:

   ```
   Beyond the Sword/Mods/Chronicles of Mankind/Assets/XML/Text/
   ```

4. W opcjach gry ustaw język Polski. Czcionki zostaw bez zmian (Sylfaen).

Możesz też pobrać [CoM-PL-v0.2.zip](https://github.com/Greywolf-Forge/CoM-PL/releases/download/v0.2/CoM-PL-v0.2.zip), rozpakować go do osobnego katalogu i skopiować wyłącznie znajdujący się w nim katalog `Assets` do katalogu moda. Przy aktualizacji zastąp poprzedni plik `ZZZ_GreywolfForge_Polish.xml` nową wersją.

Żeby odinstalować, usuń ten jeden plik. Nic innego w modzie się nie zmienia.

### Dla autorów modów

Plik ma 17 832 wpisy, tylko Tag i Polish, razem z polami gramatycznymi, których wymaga Civ4. Bez angielskiego, bez innych języków i bez danych mechaniki. Możesz dołączyć go jako osobny XML albo scalić polskie pola po Tag. Jeśli masz inną wersję moda, najpierw sprawdź kolizje kluczy.

W [`manifest.json`](manifest.json) jest wersja moda, liczba wpisów, SHA-256 i rozstrzygnięte konflikty.

### Licencja

Tłumaczenia i poprawki Greywolf Forge są na licencji MIT, patrz [LICENSE](LICENSE). Możesz ich używać w swoim modzie i zmieniać je bez pytania o zgodę. Część tekstów pochodzi od wcześniejszych tłumaczy moda. Ta licencja ich nie obejmuje, prawa zostają przy autorach.

### Testy

Wersja 0.2 przeszła wszystkie **46 testów statycznych i integracyjnych**, obejmujących strukturę XML, klucze, parametry, liczby, kodowanie i sumy plików. Nie ma nierozstrzygniętych różnic dotyczących liczb ani znaczników gry. Format nakładki był wcześniej sprawdzony pod Wine/Xvfb z polskimi ustawieniami regionalnymi. Tego wydania nie testowano w uruchomionej grze ani na natywnym Windows 10/11. Jeśli widzisz brakujący tekst albo zepsute polskie znaki (ę, ń), [zgłoś to](https://github.com/Greywolf-Forge/CoM-PL/issues/new/choose). Możesz też napisać do nas na [Discordzie](https://discord.gg/TYcdct6fTn).

Obsługiwana jest tylko wersja 1.3.3. Inne wersje mogą się nie zgadzać.

Nieoficjalne tłumaczenie fanowskie. Oryginalny mod: https://forums.civfanatics.com/forums/civ4-chronicles-of-mankind.628/
