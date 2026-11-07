# Changelog

## 0.3 (2026-11-07)

### English

- 123 confirmed English correction groups in 18 source records: 53 mechanics, 25 arithmetic, 7 factual, 18 version-specific and 20 language groups. 187 exact replacement rules affect 201 literal occurrences.
- Targeted audit of 25 English Tags; six optional editorial suggestions remain deferred. Historical article context, author voice and complete text are retained.
- Exact published v0.2 Polish retained, including grammar and duplicate-occurrence handling.
- Source- and DLL-bound installer creates a new independent mod copy. Runtime text keeps original filenames; separate English/Polish ZZZ records are maintainer exchange files outside active Assets.
- Comment-aware field matching preserves commented XML. Three explicitly approved formatting repairs are bound by exact ordered-token hashes; printf parameters, icons, colours and links remain protected.
- 70/70 automated tests pass, plus final full-copy installation and English/Polish Wine/Xvfb loading. Polish glyphs verified with original-theme Arial fallback in pl-PL/ACP1250. Native Windows and campaigns are not covered.
- CoM source encoding is normalized from declared ISO-8859-1 to UTF-8 where required, preserving decoded field values; existing accent-display improvements are recorded separately from logical English corrections.

### Polski

- 123 grupy korekt English, 18 wpisów i 201 poprawianych wystąpień; zachowane kompletne teksty oraz kontekst historycznych wersji.
- Polish zgodny bajt w bajt z v0.2. Nowa instalacja tworzy osobną kopię moda i weryfikuje SHA źródeł oraz DLL.
- Rzeczywiste testy loadera zastąpiły założenie o priorytecie nazwy ZZZ. Oddzielne pliki językowe służą autorom, a instalator aktualizuje teksty pod oryginalnymi nazwami.
- 70/70 testów PASS, instalacja pełnej kopii i testy obu języków na izolowanym Wine/Xvfb. Szczegóły i ograniczenia w dokumentacji QA.

## 0.2 (2026-11-07)

### Polski

Pełna korekta redakcyjna polskiego tłumaczenia. Poprawki w **9 973 wpisach** względem wersji 0.1.1.

- Sprawdzone komunikaty interfejsu, dyplomacja, Cywilopedia oraz opisy jednostek, budynków, ustrojów i technologii.
- Poprawione błędy znaczenia, składnia, odmiana, terminologia i brakujące szczegóły źródłowe.
- Ukończone pełne poradniki strategiczne, w tym gospodarka, badania, budynki i jednostki unikatowe oraz poradnik WoundedKnighta. Zachowano przykłady, autorskie uwagi i humor.
- Mechanika i rachunki w poradnikach zweryfikowane według właściwych historycznych wersji SDK/XML. Błędy oryginału oraz uzasadnione zmiany liczb i znaczników mają odrębne rozstrzygnięcia.
- Zachowane klucze Tag, pola gramatyczne i format nakładki. Publiczny XML zawiera wyłącznie Tag i Polish, bez zmiany danych rozgrywki ani pozostałych języków.

Wspólny przegląd **RoM-PL i CoM-PL** objął **17 613 / 17 613 grup tekstów**, **34 174 / 34 174 pól Polish** i **515 / 515 stron przeglądu**. Każdy tekst ma pełny odczyt źródła, poprzedniego tłumaczenia i wersji końcowej oraz niezależną recenzję.

Dla tego projektu: **46/46 testów statycznych i integracyjnych PASS**, zero nierozstrzygniętych różnic liczb i znaczników. Wersji 0.2 nie testowano w uruchomionej grze ani na natywnym Windows 10/11.

### English

Complete editorial review of the Polish translation. Corrected **9,973 entries** compared with version 0.1.1.

- Reviewed interface messages, diplomacy, Civilopedia, and unit, building, civic and technology descriptions.
- Corrected mistranslations, grammar, terminology and missing source details.
- Completed the full strategy guides, including economy, research, unique buildings and units, and the WoundedKnight guide. Preserved examples, personal remarks and humor.
- Checked mechanics and calculations in the guides against the appropriate historical SDK/XML versions. Original-source errors and justified numeric or token changes have individual recorded decisions.
- Preserved Tag keys, grammar fields and the overlay format. The public XML contains only Tag and Polish, without changing gameplay data or other languages.

The combined **RoM-PL and CoM-PL** review covered **17,613 / 17,613 text groups**, **34,174 / 34,174 Polish fields** and **515 / 515 review pages**. Every text has a complete reading of the source, previous translation and final version, plus an independent review.

For this project: **46/46 static and integration tests passed**, with zero unresolved numeric or runtime-token differences. Version 0.2 has not been tested in a running game or on native Windows 10/11.

## 0.1.1 (2026-11-05)

### Polski

Korekta 1843 wpisów względem wersji 0.1.

- Poprawiona pisownia, odmiana i składnia w komunikatach, dyplomacji oraz Cywilopedii.
- Poprawione polskie wielkie litery, m.in. „WOJNę” → „WOJNĘ”.
- Usunięte uszkodzone znaki dawnego kodowania i zbędne długie pauzy. Zakresy liczb i znaczniki gry zachowano.
- Przetłumaczone wykryte francuskie i angielskie pola zapisane jako Polish.
- Poprawione wybrane nazwy oraz opisy, które pomijały efekty lub nie odpowiadały źródłu.
- Zachowane klucze Tag, pola gramatyczne i format nakładki. Parametry, ikony oraz liczby sprawdzono względem starego tekstu lub właściwego źródła.

Cała nakładka przeszła kontrolę XML, kluczy, znaków i sum SHA-256. Zmienione pola mają przypisane źródło i uzasadnienie. Ręczna redakcja objęła wskazane błędy i wytypowane teksty; nie oznacza to pełnej korekty redakcyjnej każdego artykułu.

Wersja 0.1.1 nie była testowana w uruchomionej grze ani na natywnym Windows 10/11.

### English

Corrected 1843 entries compared with version 0.1.

- Fixed spelling, grammar and phrasing in interface text, diplomacy and Civilopedia articles.
- Fixed Polish uppercase letters and damaged legacy punctuation.
- Translated detected French and English content in Polish fields.
- Corrected selected names, missing source details and inaccurate descriptions.
- Preserved Tag keys, grammar fields and the overlay format. Checked parameters, icons and numbers against the previous text or the authoritative source.

The whole overlay passed XML, key, character and SHA-256 checks. Changed fields have recorded sources and reasons. Manual review covered identified issues and selected texts; it was not a complete editorial reading of every article.

Version 0.1.1 has not been tested in a running game or on native Windows 10/11.

## 0.1 (2026-11-04)

Pierwsze publiczne wydanie nakładki Polish. / Initial public Polish overlay.
