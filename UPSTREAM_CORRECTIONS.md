# CoM-PL: upstream English corrections

## For Mod Authors

Greywolf Forge supplies narrowly scoped, source-verified corrections to the English texts shipped with this mod. Each correction group below can be adopted when the original fragment and source revision match; apply all fragments of a selected group together. Keep historical version notes with the formulas or examples they qualify. No gameplay code or data is changed.

The canonical catalogue is [`patches/english-corrections-v0.3.json`](patches/english-corrections-v0.3.json). It binds each change to a source file, Tag, zero-based occurrence and SHA-256. The complete corrected English entries are in [`upstream/ZZZ_GreywolfForge_English.xml`](upstream/ZZZ_GreywolfForge_English.xml). These are exchange records for merging by Tag and occurrence, not a second drop-in runtime overlay.

Historical guides keep their original version context, author voice, examples and structure. We do not replace an older ruleset with current mod mechanics merely because the values differ. Unverified historical claims and optional stylistic changes are listed separately below.

For questions or counterexamples, please open an issue in [the CoM-PL repository](https://github.com/Greywolf-Forge/CoM-PL/issues), including the correction ID, mod version and relevant source.

## Scope

Target: **1.3.3**, Civilization IV: Beyond the Sword 3.19.

Confirmed correction groups: **123**, affecting **18 source records**. A group can contain multiple related literal edits. This is a targeted audit, not a claim that all English text has been proofread.

Primary file hashes, selected XML facts, SDK function identities, calculations and independent-review decisions are recorded in [the evidence register](docs/EVIDENCE-v0.3.json). SDK bodies and game binaries are not redistributed.

Displayed fragments omit trailing whitespace. The catalogue retains the exact matched strings, including whitespace.

English coverage: **25 unique Tags** — 16 complete short entries, 7 complete articles and 2 articles reviewed only in selected passages.

| Category | Correction groups |
| --- | ---: |
| `FACTUAL_ERROR` | 7 |
| `LANGUAGE_ERROR` | 20 |
| `MATH_ERROR` | 25 |
| `MECHANICS_ERROR` | 53 |
| `VERSION_SPECIFIC` | 18 |

Formatting exceptions are limited to one malformed BOLD closing token and two NEWLINE separators for explanatory version/math notes. Full ordered-token hashes bind these exceptions; printf parameters, icons, colours and all other tokens remain exact.

## Confirmed corrections

### fishing-town-no-ferry

- **Tag:** `TXT_KEY_BUILD_FISHING_TOWN_NO_FERRY`
- **Source:** `Chronicles_Improvements.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b6f69f866e2826295f182df49c1f075bbf9fb6de73209a82e7055dd5e5ee0a43`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(with Ferry)
```

**Corrected English fragment:**

```text
(without Ferry)
```

BUILD_FISHING_TOWN_NO_FERRY creates IMPROVEMENT_FISHING_TOWN with RouteType NONE. The separate BUILD_FISHING_TOWN has RouteType ROUTE_FERRY. The two action labels should distinguish these operations.

**Verification:**

- `Assets/XML/Units/CIV4BuildInfos.xml`; BUILD_FISHING_TOWN_NO_FERRY and BUILD_FISHING_TOWN
  SHA-256: `b7d748f96f5399b9b4c0f76e37655590e1ba7eb2b9cf853d0de9fad19d8b6b31`.
  Both create IMPROVEMENT_FISHING_TOWN; NO_FERRY has RouteType NONE; ordinary action has RouteType ROUTE_FERRY.

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### hostile-takeover-name

- **Tag:** `TXT_KEY_EVENTTRIGGER_HOSTILE_TAKEOVER_DONE`
- **Source:** `EVENTS.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `12ddd4632954d13a2adb9fdc91c5c0d45ff8b030d445c6c8b16741bc053d16b4`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
quest of Corporate Expansion
```

**Corrected English fragment:**

```text
quest of Hostile Takeover
```

EVENTTRIGGER_HOSTILE_TAKEOVER_DONE uses this world-news text after the Hostile Takeover quest. Corporate Expansion is a different quest. Parameters and the rest of the completion message are preserved.

**Verification:**

- `Assets/XML/Events/CIV4EventTriggerInfos.xml`; EVENTTRIGGER_HOSTILE_TAKEOVER_DONE/WorldNewsTexts
  SHA-256: `7d3a8efaa6115f418a0b15ac203c04c0e86843fd3a5101413b92299dc74f0f26`.
  TXT_KEY_EVENTTRIGGER_HOSTILE_TAKEOVER_DONE
- `Assets/Python/EntryPoints/CvRandomEventInterface.py`; canTriggerHostileTakeoverDone
  SHA-256: `383299af2aaf83fdfdd18a14c2dc44a3a67b93e6d15a16b8bc52e41b9b75b8a3`.
  def canTriggerHostileTakeoverDone(argsList): 	kTriggeredData = argsList[0] 	player = gc.getPlayer(kTriggeredData.ePlayer) 	trigger = gc.getEventTriggerInfo(kTriggeredData.eTrigger) 	kOrigTriggeredData = player.getEventOccured(trigger.getPrereqEvent(0))  	listResources = getHostileTakeoverListResources(gc.getCorporationInfo(kOrigTriggeredData.eCorporation), player)  	if len(listResources) > 0: 		return False  	kActualTriggeredDataObject = player.getEventTriggered(kTriggeredData.iId) 	kActualTriggeredDataObject.eCorporation = kOrigTriggeredData.eCorporation 	kActualTriggeredDataObject.eBuilding = kOrigTriggeredData.eBuilding 	kActualTriggeredDataObject.iCityId = kOrigTriggeredData.iCityId 	kActualTriggeredDataObject.iPlotX = kOrigTriggeredData.iPlotX 	kActualTriggeredDataObject.iPlotY = kOrigTriggeredData.iPlotY  	return True

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### alternative-energy-exact-expiry

- **Tag:** `TXT_KEY_EVENT_ALTERNATIVE_ENERGY_HELP_1`
- **Source:** `EVENTS.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `12ddd4632954d13a2adb9fdc91c5c0d45ff8b030d445c6c8b16741bc053d16b4`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
if you reach the Transhuman Era
```

**Corrected English fragment:**

```text
if your team acquires Controlled Plasma, Micromechanics, Metamaterials, Artificial Intelligence, Ecological Engineering, Brain Machine Interface or Mesh Networks
```

Quest expiry uses the concrete obsolete-technology list, not an era check. The core tech graph admits other technologies from this era without any obsolete technology, and CoM calls this era Information. Resolve display labels through Description: HUMAN_MACHINE_INTERFACE is Brain Machine Interface.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/short-pending-verification.json`; alternative-energy-exact-expiry
  Audit snapshot SHA-256: `96bc62051b9404e3353d069565a95fc4e5169e2252f24adc93bb9325f6a0c7de`.

**Compatibility:** Polish and all runtime tokens preserved. Current mod data; AND2 SDK scope stated separately from CoM DLL evidence.

### guns-butter-civic

- **Tag:** `TXT_KEY_EVENT_GUNS_BUTTER_HELP_1`
- **Source:** `EVENTS.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `12ddd4632954d13a2adb9fdc91c5c0d45ff8b030d445c6c8b16741bc053d16b4`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
[COLOR_HIGHLIGHT_TEXT]Vassalage[COLOR_REVERT]
```

**Corrected English fragment:**

```text
[COLOR_HIGHLIGHT_TEXT]Nobility[COLOR_REVERT]
```

canApplyGunsButterDone2 tests CIVIC_ARISTOCRACY. Its Description is TXT_KEY_CIVIC_ARISTOCRACY, whose English label is Nobility in this mod. Vassalage is the old BtS label and names the wrong mod civic.

**Verification:**

- `Assets/Python/EntryPoints/CvRandomEventInterface.py`; canApplyGunsButterDone2
  SHA-256: `383299af2aaf83fdfdd18a14c2dc44a3a67b93e6d15a16b8bc52e41b9b75b8a3`.
  def canApplyGunsButterDone2(argsList): 	iEvent = argsList[0] 	kTriggeredData = argsList[1] 	player = gc.getPlayer(kTriggeredData.ePlayer)  	iCivic = gc.getInfoTypeForString("CIVIC_ARISTOCRACY")  	if not player.isCivic(iCivic): 		return False  	return True
- `Assets/XML/GameInfo/CIV4CivicInfos.xml`; CIVIC_ARISTOCRACY/Description
  SHA-256: `cefdc5571cec8e1c0242e5923e188b36d384382a5272704a6dbd9dbaff6c9b16`.
  TXT_KEY_CIVIC_ARISTOCRACY
- `Assets/XML/Text/CIVICS.xml`; TXT_KEY_CIVIC_ARISTOCRACY/English
  SHA-256: `32d8080295f9544c721e966f6f4e3cf7c03600c7827d4a53fe0f26cf3e640496`.
  Nobility

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### industrial-action-civic

- **Tag:** `TXT_KEY_EVENT_INDUSTRIAL_ACTION_2_HELP`
- **Source:** `EVENTS.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `12ddd4632954d13a2adb9fdc91c5c0d45ff8b030d445c6c8b16741bc053d16b4`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
[COLOR_NEGATIVE_TEXT]State Property[COLOR_REVERT]
```

**Corrected English fragment:**

```text
[COLOR_NEGATIVE_TEXT]Planned[COLOR_REVERT]
```

canDoIndustrialAction2 excludes CIVIC_PLANNED. Its Description resolves to the English label Planned. State Property is an obsolete base-game reference. The event condition is unchanged.

**Verification:**

- `Assets/Python/EntryPoints/CvRandomEventInterface.py`; canDoIndustrialAction2
  SHA-256: `383299af2aaf83fdfdd18a14c2dc44a3a67b93e6d15a16b8bc52e41b9b75b8a3`.
  def canDoIndustrialAction2(argsList):  	iEvent = argsList[0] 	kTriggeredData = argsList[1] 	pPlayer = gc.getPlayer(kTriggeredData.ePlayer)  	if pPlayer.isCivic(gc.getInfoTypeForString("CIVIC_PLANNED")): 		return False  	return True
- `Assets/XML/GameInfo/CIV4CivicInfos.xml`; CIVIC_PLANNED/Description
  SHA-256: `cefdc5571cec8e1c0242e5923e188b36d384382a5272704a6dbd9dbaff6c9b16`.
  TXT_KEY_CIVIC_PLANNED
- `Assets/XML/Text/CIVICS.xml`; TXT_KEY_CIVIC_PLANNED/English
  SHA-256: `32d8080295f9544c721e966f6f4e3cf7c03600c7827d4a53fe0f26cf3e640496`.
  Planned

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### sports-league-com-exact-expiry

- **Tag:** `TXT_KEY_EVENT_SPORTS_LEAGUE_HELP_1`
- **Source:** `EVENTS.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `12ddd4632954d13a2adb9fdc91c5c0d45ff8b030d445c6c8b16741bc053d16b4`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
if you reach the Modern Era
```

**Corrected English fragment:**

```text
if your team acquires Aerodynamics, Electronics, Globalization or Antibiotics
```

CoM displays ERA_MODERN as Atomic and its core tech graph admits several technologies from that era without any quest-obsolete technology. Use the exact targets; ADVANCED_FLIGHT and MODERN_HEALTH_CARE display as Aerodynamics and Antibiotics.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/short-pending-verification.json`; sports-league-com-exact-expiry
  Audit snapshot SHA-256: `96bc62051b9404e3353d069565a95fc4e5169e2252f24adc93bb9325f6a0c7de`.

**Compatibility:** Polish and all runtime tokens preserved. Current mod data; AND2 SDK scope stated separately from CoM DLL evidence.

### trade-naming-option

- **Tag:** `TXT_KEY_BUG_OPT_UNITNAMING__COMBAT_TRADE_HOVER`
- **Source:** `INTERFACE.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `de9411d99179794f873798602cb766c7a34b143c3ddb6b0b1f74005d671b065e`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
'EXECUTIVES'
```

**Corrected English fragment:**

```text
'TRADE'
```

The option and UI binding are Combat_TRADE. Combat_EXECUTIVES is a separate setting; copying its name into this tooltip describes the wrong control.

**Verification:**

- `Assets/Config/Unit Naming.xml`; option[@id="Combat_TRADE"] and option[@id="Combat_EXECUTIVES"]
  SHA-256: `837731e20c9098d220d7d5b39b73b9307399ee63c4f6fd0d69adaf56952c2939`.
- `Assets/Python/BUG/Tabs/BugUnitNameOptionsTab.py`; create
  SHA-256: `e523082be6a9c8403c407b62a1cd36afcf116234a8da280af2399cb0388d1b22`.
  self.addTextEdit(screen, columnL, columnR, "UnitNaming__Combat_TRADE")

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### naming-counter-tt2

- **Tag:** `TXT_KEY_BUG_OPT_UNITNAMING__DEFAULT_HOVER`
- **Source:** `INTERFACE.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `de9411d99179794f873798602cb766c7a34b143c3ddb6b0b1f74005d671b065e`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
tt1[f][x][COLOR_REVERT] - Count from x
```

**Corrected English fragment:**

```text
tt2[f][x][COLOR_REVERT] - Count from x
```

The secondary counter is tt2, while tt1 has a range argument [x:y]. The example must use the token accepted by getTotal2 and swapCountCode. This changes the documented code, not the parser.

**Verification:**

- `Assets/Python/Contrib/UnitNameEventManager.py`; getTotal2; swapCountCode
  SHA-256: `4b9921d6195b379168d0ac83fd851fb7ca3a426ba3c7db2a4060d91102474b13`.
  getTotal2 finds "^tt2["; swapCountCode(zsName, "^tt2", ziTT2).

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### synthetic-fuels-resource

- **Tag:** `TXT_KEY_LOCAL_SYNTHETIC_FUELS_4`
- **Source:** `MISC.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `714c2d660544ef4ffd429fa0b1e9f08c9ee06198a859ab3f800655ab2f34a3fc`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
+1 oil resource
```

**Corrected English fragment:**

```text
+1 Oil Products resource
```

EVENT_SYNTHETIC_FUELS_4 calls doSyntheticFuels4 and displays this LocalInfoText. The callback grants one BONUS_DIESEL, whose English Description is Oil Products, not Oil.

**Verification:**

- `Assets/Python/EntryPoints/CvRandomEventInterface.py`; doSyntheticFuels4
  SHA-256: `383299af2aaf83fdfdd18a14c2dc44a3a67b93e6d15a16b8bc52e41b9b75b8a3`.
  def doSyntheticFuels4(argsList): 	iEvent = argsList[0] 	kTriggeredData = argsList[1]  	pPlayer = gc.getPlayer(kTriggeredData.ePlayer) 	pCity = pPlayer.getCity(kTriggeredData.iCityId)  	iBonus = gc.getInfoTypeForString("BONUS_DIESEL")  	pCity.changeFreeBonus(iBonus, 1)  	return 1   ####### ALTERNATIVE_ENERGY ######
- `Assets/XML/Events/CIV4EventInfos.xml`; EVENT_SYNTHETIC_FUELS_4
  SHA-256: `6e672ce8f985eb666422a188ab16587b7e24dee7bcc46018c82f473a3342a8ab`.
  PythonCallback=doSyntheticFuels4; LocalInfoText=TXT_KEY_LOCAL_SYNTHETIC_FUELS_4
- `Assets/XML/Terrain/CIV4BonusInfos.xml`; BONUS_DIESEL/Description
  SHA-256: `f73c4f5f48415ddf3c0e56dcce7ee3e0191f87b99200aebf8f68e5974ee18ae3`.
  TXT_KEY_BONUS_DIESEL
- `Assets/XML/Text/RESSOURCES.xml`; TXT_KEY_BONUS_DIESEL/English
  SHA-256: `7156ee5a47b1538f14cd5ab9e845bafcfbbf8dfac79598f51c6aaff675a040d8`.
  Oil Products

**Compatibility:** Applies to this installed mod version; do not replace base BtS civic names globally. Text only; no game data changes.

### research-commerce-remainder

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
So, yes, you WILL get AT LEAST one gold from each city that has a commerce that is not a multiple of 10, if your science or culture is not 100%.
```

**Corrected English fragment:**

```text
With culture at 0% and research below 100%, this rounding gives at least one gold from a city whose commerce is not a multiple of 10. The same applies with research at 0% and culture below 100%. It is not guaranteed when both sliders are active: 5 commerce at 60% research and 40% culture leaves no gold.
```

The universal claim fails when both sliders are active: 5 commerce at 60% research and 40% culture yields 3 research, 2 culture and no gold.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; commerce_remainder_counterexample
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Arithmetic under the article's own flooring model.

### research-floor-definition

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
FLOOR means rounding DOWN to the nearest integer AND it has higher precedence than all other operators EXCEPT FOR parentheses. You will see it used a lot in the article.
```

**Corrected English fragment:**

```text
FLOOR means rounding DOWN to the nearest integer. First evaluate the expression inside its parentheses, then round that result down; evaluate nested FLOOR calls from the inside out. You will see it used a lot in the article.
```

FLOOR is a function, not an infix operator with the asserted precedence. Its argument must be evaluated before truncation, and nested calls work inside out.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/source-manifest.json`; Group 13012 FLOOR examples
  Audit snapshot SHA-256: `14a15b68c64cefbf2c2d50280fb8ac3d04e5ea58a9084d98a080d999f3bdbca3`.

**Compatibility:** Mathematical notation used throughout the historical article.

### research-historical-scope

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
- by [BOLD]Requies[\BOLD]
```

**Corrected English fragment:**

```text
- by [BOLD]Requies[\BOLD]. Version note: this historical article describes the author's model of early vanilla Civilization IV. It is not a verified description of later versions. Vanilla 1.61 already adds the known-team and prerequisite bonuses to a common base, counts living teams, awards prerequisite bonuses for known OR prerequisites, calculates team research costs differently, and normalizes overflow. Keep the formulas and overflow advice below in their historical context; do not apply them directly to Warlords, Beyond the Sword or mods.
```

The article presents an early-vanilla model as generally applicable. Vanilla 1.61 already uses additive research bonuses, living-team counts and normalized overflow. Preserve the historical model while explicitly limiting its applicability.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; vanilla161/CvPlayer::calculateResearchModifier, CvTeam::getResearchCost and CvTeam::setResearchProgress
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.

**Compatibility:** Historical early-vanilla article; contrasted with directly inspected vanilla 1.61 SDK.

### research-overflow-1048-equation

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
104.8% ((1 + 17 known civs w/ tech/18 civs) * 1.6 [tech w/ 3 optional prerequisites])
```

**Corrected English fragment:**

```text
104.8% (((1 + RDDW (0.30 * 17 known civs w/ tech / 18 civs)) * 1.6 - 1) * 100 [tech w/ 3 optional prerequisites])
```

The original expression omits the 0.30 known-team coefficient and the subtraction/conversion needed to express a percentage gain. With two-decimal truncation the historical expression gives 104.8%.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; historical_overflow_percentage
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Arithmetic correction inside the retained historical overflow model; not applicable as vanilla 1.61 overflow advice.

### research-overflow-prereq-arithmetic

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
1.6 (1.2 * 3)
```

**Corrected English fragment:**

```text
1.6 (1 + 0.2 * 3)
```

1.2 times 3 is 3.6, not 1.6. The article's three-prerequisite multiplier is 1 + 0.2 times 3.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; prerequisite_multiplier
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Arithmetic correction inside the retained historical model.

### research-table-rounding-scope

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
[H2]Additional Modifier for knowing 1 more civilization who has the tech out of....[\H2]
```

**Corrected English fragment:**

```text
[H2]Additional modifier before rounding: 0.30 divided by the number of starting civilizations[\H2][NEWLINE]These values are unrounded. In the historical model above, truncate the total known-civilization bonus to hundredths; the actual marginal increase can depend on how many known civilizations already have the technology.
```

The table lists 0.30/N before hundredth truncation. The actual change in a truncated modifier depends on how many known civilizations already have the technology, so these values are not fixed final marginal bonuses.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; research_table_rounding_counterexample
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Internal arithmetic of the preserved historical model.

### research-tech-filename

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Assets\XML\Technologies\CIV4TechInfo.xml
```

**Corrected English fragment:**

```text
Assets\XML\Technologies\CIV4TechInfos.xml
```

The actual technology definitions filename is plural CIV4TechInfos.xml.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; vanilla 1.61 technology definitions source paths
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.

**Compatibility:** Vanilla 1.61 XML filename.

### research-unclosed-formulas

- **Tag:** `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
[BOLD]Tech Known by Civilizations modifier[\BOLD] = 1 + RDDW (0.30 * [BOLD]# known Civs who have the tech[\BOLD] / [BOLD]# of Civs who started the game[\BOLD]
```

**Corrected English fragment:**

```text
[BOLD]Tech Known by Civilizations modifier[\BOLD] = 1 + RDDW (0.30 * [BOLD]# known Civs who have the tech[\BOLD] / [BOLD]# of Civs who started the game[\BOLD])
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
FLOOR (FLOOR ((37 + 1) * (1 + RDDW (0.30 * 3 / 7))) * (1 + 0.2 + (0.2 * 0))
```

**Corrected English fragment:**

```text
FLOOR (FLOOR ((37 + 1) * (1 + RDDW (0.30 * 3 / 7))) * (1 + 0.2 + (0.2 * 0)))
```

Each displayed expression has one unmatched opening parenthesis. Closing it preserves the historical formula.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; formula_parenthesis_balance
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Internal mathematical syntax only; not endorsement of the historical research model.

### se-liberalism-chain

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Paper-Education-Library sequence
```

**Corrected English fragment:**

```text
Paper-Education-Liberalism sequence
```

Library is a building. The named research sequence is Paper, Education, Liberalism; XML confirms the relevant prerequisites.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; TECH_LIBERALISM, TECH_EDUCATION
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.

**Compatibility:** Vanilla 1.61 technology tree.

### se-monastery-religion

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
I put a question mark by monasteries since they may not be possible to build if you didn't found a religion.
```

**Corrected English fragment:**

```text
I put a question mark by monasteries since the relevant religion must be present in the city; you do not need to have founded it.
```

Monasteries require the relevant religion in the city. Founding the religion is not required.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; BUILDING_CHRISTIAN_MONASTERY PrereqReligion
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.

**Compatibility:** Vanilla 1.61 building prerequisites.

### se-oxford-map-size

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
which requires 6 universities (which, in turn,
```

**Corrected English fragment:**

```text
which requires 6 universities on a Standard map outside One City Challenge (which, in turn,
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
You need 6 Universities to build Oxford which will use the 'extra' cities
```

**Corrected English fragment:**

```text
On a Standard map outside One City Challenge, you need 6 Universities to build Oxford, which will use the 'extra' cities
```

Six universities is the normal Standard-map requirement, not a universal constant. XML supplies base four and Standard +50%; SDK applies the map modifier and caps the prerequisite at one for a human player in One City Challenge.

Classified as MECHANICS_ERROR in the final catalogue: the qualification concerns map size and One City Challenge settings, not a change between game versions. The independently reviewed English is unchanged.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; BUILDING_OXFORD_UNIVERSITY and WORLDSIZE_STANDARD
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; vanilla161/CvPlayer::getBuildingClassPrereqBuilding
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.

**Compatibility:** Vanilla 1.61, Standard map outside One City Challenge; other map sizes vary and human OCC caps the requirement at one.

### se-philosophical-additive-bonus

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
for the double Great Person Points (GPP) and also for the cheaper University
```

**Corrected English fragment:**

```text
for the +100% Great Person Points (GPP) rate, added to other percentage bonuses, and also for the cheaper University
```

Philosophical adds +100% to the GPP rate; it doubles the base only when there are no other rate modifiers. It does not multiply the final modified rate by two.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; TRAIT_PHILOSOPHICAL iGreatPeopleRateModifier=100
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-sdk-evidence.json`; CvCity::getTotalGreatPeopleRateModifier, vanilla1.61 and installed-BtS
  Audit snapshot SHA-256: `1eaa07f0020725be83160790ebe188e5e890d44ac9f074493c08136cb828538a`.

**Compatibility:** Historical vanilla 1.61; also confirmed in installed BtS SDK.

### se-search-typo

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Spcialist Economy
```

**Corrected English fragment:**

```text
Specialist Economy
```

Fix the misspelled search phrase so readers can search for Specialist Economy.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/source-manifest.json`; Group 13016 exact English
  Audit snapshot SHA-256: `14a15b68c64cefbf2c2d50280fb8ac3d04e5ea58a9084d98a080d999f3bdbca3`.

**Compatibility:** Textual spelling correction.

### se-specialist-slot-scope

- **Tag:** `TXT_KEY_STRATEGY_SE_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Specialists can only be assigned if certain buildings exist (e.g. Library enables two Scientists).
```

**Corrected English fragment:**

```text
Non-Citizen specialists normally require available slots, usually supplied by buildings (e.g. a Library enables two Scientists); ordinary Citizens do not require a building.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Caste System eliminates the restrictions for item 3, but conflicts with Slavery
```

**Corrected English fragment:**

```text
Caste System eliminates the slot restrictions for Artists, Scientists and Merchants, but conflicts with Slavery
```

Ordinary Citizens do not require specialist buildings. Caste System removes slot limits only for Artists, Scientists and Merchants; it does not make all specialist types unlimited.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; CIVIC_CASTE_SYSTEM SpecialistValids; SPECIALIST_CITIZEN
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.

**Compatibility:** Vanilla 1.61 rules.

### ub-assembly-coal-cost

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 2.**

**Original English fragment:**

```text
has double production speed with coal.
```

**Corrected English fragment:**

```text
has a +50% production bonus with coal.
```

**Fragment 2; exact occurrences: 2.**

**Original English fragment:**

```text
double production with coal
```

**Corrected English fragment:**

```text
get a +50% production bonus with coal
```

**Fragment 3; exact occurrences: 2.**

**Original English fragment:**

```text
With the Assembly Plant costing 250 hammers and having two double speeds bonuses, it would be like building these babies for 62 hammers!
```

**Corrected English fragment:**

```text
With the Assembly Plant costing 250 hammers, Organized gives +100% and coal gives +50%; together that is +150%, so these babies nominally need 100 base hammers before other modifiers and per-turn rounding!
```

**Fragment 4; exact occurrences: 2.**

**Original English fragment:**

```text
for a quarter of the cost
```

**Corrected English fragment:**

```text
for two-fifths of the nominal base cost before other modifiers
```

Both Warlords and BtS give the Assembly Plant +50% with coal and +100% for Organized. SDK construction modifiers add rather than multiply: 250/(1+1+0.5)=100 base hammers. Correct every repeated claim without consolidating the original duplicated sections.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: BUILDING_GERMAN_ASSEMBLY_PLANT in Warlords and BtS
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; sdk: CvCity::getProductionModifier(BuildingTypes), CvPlayer::getProductionModifier(BuildingTypes), CvCity::getBaseYieldRateModifier
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.assembly_organized_coal_base_hammers
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-assembly-engineer-slots

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
To a total of 50% hammer increase from buildings (forge and factory), you can add +50% from power (supplied by the either hydro, coal or nuclear plants, but the Three Gorges Dam can be more economical), +100% from the Ironworks (+50% each for iron and coal), +50% from Bureaucracy. With some good food sources you will max out your six engineers
```

**Corrected English fragment:**

```text
To a total of 50% hammer increase from buildings (forge and factory), you can add +50% from power (supplied by the either hydro, coal or nuclear plants, but the Three Gorges Dam can be more economical), +100% from the Ironworks (+50% each for iron and coal), +50% from Bureaucracy. With some good food sources you will max out your eight engineers
```

The Forge contributes one Engineer slot, the Assembly Plant four and Ironworks three, for eight. The Shale Plant paragraph correctly has six with an ordinary Factory and is deliberately left unchanged.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: BUILDING_FORGE, BUILDING_GERMAN_ASSEMBLY_PLANT and BUILDING_IRON_WORKS/SpecialistCounts
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.engineer_slots_forge_assembly_ironworks
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-assembly-production-conditions

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 2.**

**Original English fragment:**

```text
Don't forget the +25 bonus for OR and the +100% for having a special resource when building buildings.
```

**Corrected English fragment:**

```text
Don't forget the +25% bonus for OR in cities with the state religion and a possible +100% resource bonus for eligible buildings.
```

**Fragment 2; exact occurrences: 2.**

**Original English fragment:**

```text
You can also have a laboratory that gives +50% bonus in addition to +100% again for having a resource.
```

**Corrected English fragment:**

```text
For eligible spaceship parts, a laboratory adds +50% and the appropriate resource can add another +100%.
```

Organized Religion needs the state religion in the city; a resource construction bonus is target-specific, and the Laboratory production bonus applies to spaceship parts rather than all projects. These qualifications make the adjacent worked sums meaningful.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; sdk: CvCity::getProductionModifier(BuildingTypes)
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: BUILDING_LABORATORY/iSpaceProductionModifier
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.assembly_capital_eligible_spaceship
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-assembly-production-sums

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
for a total of around +385% or +410%.
```

**Corrected English fragment:**

```text
for totals of +375% or +400% on eligible buildings or spaceship parts, respectively.
```

The stated capital base bonus is +250%. Adding the stated +125% or +150% gives +375% or +400%, not +385% or +410%. The construction/resource and Laboratory bonuses only apply to eligible targets.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.assembly_capital_eligible_building
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.assembly_capital_eligible_spaceship
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: BUILDING_LABORATORY/iSpaceProductionModifier
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-feitoria-mercantilism

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
the Customs House would be useless if running Mercantilism, thereby closing all foreign trade routes.
```

**Corrected English fragment:**

```text
the Customs House would usually be of little use under Mercantilism, which closes ordinary foreign trade routes; routes with a master or vassal remain possible in BtS 3.19.
```

BtS 3.19 canHaveTradeRoutesWith accepts master/vassal trade before checking the no-foreign-trade civic flag. Qualify the absolute statement and identify the checked version.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; sdk: CvPlayer::canHaveTradeRoutesWith
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-feitoria-trade-modifier

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
it grants a 50% boost to all [BOLD]foreign[\BOLD] trade coming in from [BOLD]overseas[\BOLD].
```

**Corrected English fragment:**

```text
in BtS 3.19 it grants a +100% trade-route modifier to all [BOLD]foreign[\BOLD] routes, whether or not they come from [BOLD]overseas[\BOLD].
```

The current original BtS XML gives Custom House and Feitoria a +100% foreign trade-route modifier. CvCity::totalTradeModifier applies the foreign modifier independently of the overseas modifier. Label the checked version because the historical article may have been written against earlier expansion data.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: BUILDING_PORTUGAL_FEITORIA and BUILDING_CUSTOM_HOUSE/iForeignTradeRouteModifier
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; sdk: CvCity::totalTradeModifier
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-gallic-maceman-costs

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
[COLOR_YIELD_COMMERCE]Gallic Warrior[COLOR_REVERT][TAB]60[TAB]6
```

**Corrected English fragment:**

```text
[COLOR_YIELD_COMMERCE]Gallic Warrior[COLOR_REVERT][TAB]40[TAB]6
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
[COLOR_YIELD_COMMERCE]Maceman[COLOR_REVERT][TAB][TAB]80[TAB]8
```

**Corrected English fragment:**

```text
[COLOR_YIELD_COMMERCE]Maceman[COLOR_REVERT][TAB][TAB]70[TAB]8
```

The standard-speed base costs are 40 for the Gallic Warrior and 70 for the Maceman in both checked expansions. These table cells are not game-speed-adjusted prices.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: UNIT_CELTIC_GALLIC_WARRIOR and UNIT_MACEMAN/iCost in Warlords and BtS
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-khmer-spelling

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Khymer Baray
```

**Corrected English fragment:**

```text
Khmer Baray
```

Correct the civilization name in the section heading.

**Verification:**

- `Assets/XML/Text/STRATEGIES_PEDIA.xml`; TXT_KEY_STRATEGY_UB_PEDIA/English
  SHA-256: `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`.
  Direct inspection of the English wording; no gameplay claim introduced.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-machine-gun-bonus

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
[COLOR_RED]Machine Gun[COLOR_REVERT][TAB]125[TAB]18[TAB]1[TAB]Can only defend, 1st Strike[NEWLINE][TAB][TAB][TAB][TAB][TAB][TAB]+25% vs. Gunpowder Units
```

**Corrected English fragment:**

```text
[COLOR_RED]Machine Gun[COLOR_REVERT][TAB]125[TAB]18[TAB]1[TAB]Can only defend, 1st Strike[NEWLINE][TAB][TAB][TAB][TAB][TAB][TAB]+50% vs. Gunpowder Units
```

Machine Guns have a +50% modifier against gunpowder units in both Warlords and BtS. Correct both identical table entries while leaving Infantry’s separate +25% modifier intact.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: UNIT_MACHINE_GUN/UnitCombatMods in Warlords and BtS
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-mall-culture-happiness

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
the broadcast tower (along with threatres and coliseums) will give +1 happiness for every 10% culture. If you have all three in a city, then that means +3 [ICON_HAPPY] for only raising the culture setting up by 10%.
```

**Corrected English fragment:**

```text
the broadcast tower and theatre each give +1 happiness for every 10% culture, while the coliseum contributes +1 per 20%. If you have all three in a city, raising the culture setting from 0% to 10% gives +2 [ICON_HAPPY] after the combined bonus is rounded down.
```

The culture happiness coefficients are 10, 10 and 5. CvCity::getCommerceHappinessByType evaluates the combined coefficient with integer division: (10+10+5)*10/100=2, not 3. Explicitly start from 0% so this is not misread as every possible ten-point slider change.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: Theatre, Colosseum and Broadcast Tower/CommerceHappinesses
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; sdk: CvCity::getCommerceHappinessByType
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.mall_happiness_slider_zero_to_ten
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-pavilion-spelling

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Chinese Pavlion
```

**Corrected English fragment:**

```text
Chinese Pavilion
```

Correct the misspelling in the section heading; retain the original writing and layout.

**Verification:**

- `Assets/XML/Text/STRATEGIES_PEDIA.xml`; TXT_KEY_STRATEGY_UB_PEDIA/English
  SHA-256: `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`.
  Direct inspection of the English wording; no gameplay claim introduced.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-sam-versioned-bonus

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
+50% vs. Helicopter Units
```

**Corrected English fragment:**

```text
+50% vs. Helicopter Units (Warlords); +75% in BtS 3.19
```

The original +50% is correct for Warlords, while the BtS 3.19 unit has +75%. Preserve the historical value and label the expansion difference instead of treating a valid older statistic as an error.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: UNIT_SAM_INFANTRY/UnitCombatMods in Warlords and BtS
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### ub-shale-production-sums

- **Tag:** `TXT_KEY_STRATEGY_UB_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
+185% in your capital (+135% out of capital)
```

**Corrected English fragment:**

```text
+160% in your capital (+110% out of capital)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
non-Captial cities are between +360% or +435%.
```

**Corrected English fragment:**

```text
non-capital cities reach +335% for eligible buildings or +410% for eligible spaceship parts.
```

Forge 25 + Factory 25 + Shale Plant 10 + power 50 gives +110%, or +160% with Bureaucracy in the capital. Outside the capital, Ironworks adds 100; eligible building bonuses add 125 for 335, while Laboratory/resource/Space Elevator add 200 for 410.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; primary_xml: Forge, Factory, Shale Plant, Ironworks, Laboratory and Space Elevator
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.shale_generic_outside_capital
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.shale_generic_capital
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.shale_ironworks_eligible_building_outside_capital
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/ub-primary-verification.json`; math.shale_ironworks_eligible_spaceship_with_elevator_outside_capital
  Audit snapshot SHA-256: `c7680078c8b240a9bddd4367d3cc529b46d9657cb8bf2b4dbff1ae3188d4c631`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-berserk-river-penalty

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
you have the advantage when laying siege to a city across a river if the enemy doesn't have Engineering. His non-mounted units cannot counter attack from the city without suffering a 20% penalty for attacking across the river.
```

**Corrected English fragment:**

```text
you have the advantage when laying siege to a city across a river. Enemy units without Amphibious, mounted or not, suffer a 25% penalty when attacking across the river; Engineering does not remove this combat penalty.
```

The river attack modifier is -25. The combat check exempts Amphibious units, not mounted units or units belonging to a player with Engineering. Road/bridge movement rules are separate from this combat penalty.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: RIVER_ATTACK_MODIFIER
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: river combat check
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-camel-versioned-withdrawal

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
higher withdrawal chance (25%)
```

**Corrected English fragment:**

```text
higher withdrawal chance (25% in vanilla/Warlords, 15% in BtS)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
(+55% withdrawal chance with Flanking II)
```

**Corrected English fragment:**

```text
(55% total withdrawal chance with Flanking I and II in vanilla/Warlords, 45% in BtS)
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
85% chance of retreating from a failed attack.
```

**Corrected English fragment:**

```text
85% chance of retreating from a failed attack in Warlords, or 75% in BtS.
```

Preserve the valid older base 25% and explicitly distinguish BtS 15%. Flanking I and II add 10+20 points; Tactics adds 30. The old +55% notation incorrectly suggests an additional bonus rather than the total.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_ARABIA_CAMELARCHER/iWithdrawalProb in all four versions
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: FLANKING1, FLANKING2 and TACTICS
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-chokonu-collateral-order

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Their first strikes also work well when defending against siege weapons, since they might be able to win before much collateral damage is suffered.
```

**Corrected English fragment:**

```text
Their first strikes also work well in the direct fight when defending against siege weapons, but cannot prevent collateral damage, which is resolved before the combat rounds.
```

resolveCombat calls collateralCombat before the combat loop, so defender first strikes cannot end the duel before its collateral damage has already been resolved.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::resolveCombat, collateralCombat call before while(true)
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-chokonu-drill-scope

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Gunpowder units can't choose Drill, so upgraded Chukonus can be interesting.
```

**Corrected English fragment:**

```text
In vanilla/Warlords, gunpowder units can't choose Drill, so upgraded Chukonus can be interesting; BtS allows them to choose Drill directly.
```

Retain the valid older promotion-inheritance advice and label the BtS change, as the article already does in its Redcoat section.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_DRILL1/UnitCombats in vanilla, Warlords and BtS
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-chokonu-tech-prerequisites

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Machinery requires Iron Working and Chukonus need the iron resource to be built
```

**Corrected English fragment:**

```text
Machinery requires Metal Casting; Chukonus also need Archery and the iron resource, which Iron Working reveals and lets you connect
```

Machinery has Metal Casting, not Iron Working, as its prerequisite. Chokonu construction needs Machinery, Archery and Iron. Retain the author’s early Iron Working advice for finding and connecting the resource.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: TECH_MACHINERY prerequisites and UNIT_CHINA_CHOKONU tech/resource prerequisites
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-conquistador-first-strikes

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
To top all of this off, Conquistadors benefit from 2 first strikes (which normal knights don't get), making them even harder to defeat.
```

**Corrected English fragment:**

```text
Like normal knights, Conquistadors are immune to first strikes; they do not have first strikes of their own.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Their first strikes and immunity to first strikes certainly help, especially against longbows.
```

**Corrected English fragment:**

```text
Their immunity to first strikes certainly helps, especially against longbows.
```

All four checked original XML versions give Conquistadors zero guaranteed first strikes, zero first-strike chances and immunity to first strikes. Correct both occurrences of the nonexistent ability.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_SPANISH_CONQUISTADOR/iFirstStrikes, iChanceFirstStrikes and bFirstStrikeImmune
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-conquistador-versioned-prerequisites

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Spain: Conquistador (Knight)
```

**Corrected English fragment:**

```text
Spain: Conquistador (Knight in vanilla/Warlords; Cuirassier in BtS)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
The Spanish player would also do well to research Guilds early, extending the life and usefulness of the UU.
```

**Corrected English fragment:**

```text
In vanilla/Warlords, the Spanish player would also do well to research Guilds early, extending the life and usefulness of the UU. In BtS, it instead requires Military Tradition and Gunpowder; Horseback Riding is required in both cases.
```

The original knight strategy is historical. BtS changes the replacement class and main technology prerequisites, while preserving Horseback Riding and the horse/iron resources. Label the versions rather than discarding the older advice.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_SPANISH_CONQUISTADOR/Class, PrereqTech and TechTypes
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-cossack-beeline-prerequisites

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
beelining to Education, getting Liberalism and choosing Nationalism as the free tech.
```

**Corrected English fragment:**

```text
beelining to Education, being the first to get Liberalism and choosing Nationalism as the free tech.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
techs needed to build Cossacks (and you must have horses, of course).
```

**Corrected English fragment:**

```text
techs that, together with Horseback Riding, are needed to build Cossacks in vanilla (and you must have horses, of course).
```

The free technology is awarded only to the first Liberalism discoverer. The original vanilla Cossack also requires Horseback Riding. Preserve the historical early-Cavalry tactic.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_RUSSIA_COSSACK/PrereqTech and TechTypes; TECH_LIBERALISM
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-cossack-cannon-attack

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(+50% against cannon and 30% withdrawal chance)
```

**Corrected English fragment:**

```text
(+50% when attacking cannon and 30% withdrawal chance)
```

The Cannon bonus is an attack-only UnitClassAttackMod, not a modifier while defending.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_RUSSIA_COSSACK/UnitClassAttackMods
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-cossack-vanilla-version

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Besides the Redcoat, the Cossack is one UU that has been changed in Warlords. In Civ IV vanilla, the Cossack has a fearsome reputation.
```

**Corrected English fragment:**

```text
Besides the Redcoat, the Cossack is one UU that has been changed in Warlords and vanilla 1.74. In Civ IV vanilla 1.61, the Cossack has a fearsome reputation.
```

Original 1.61 XML confirms strength 18, while vanilla 1.74 and both expansions have 15. Keep the old 18-strength strategy, with the correct version boundary.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_RUSSIA_COSSACK/iCombat in all four versions
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; historical_patch_provenance
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-drill-first-strikes

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
a total of 5 first strikes and a chance at another
```

**Corrected English fragment:**

```text
a total of 3 guaranteed first strikes and chances for up to 3 more
```

Drill I–IV contribute 0/1/0/2 guaranteed first strikes and 1/0/2/0 first-strike chances: totals 3 and 3. The original reverses and overstates these quantities.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_DRILL1 through PROMOTION_DRILL4
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-french-cavalry-timing

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
On this note, there's another interesting use for Musketeers. Try postponing Chemistry and beelining to Military Tradition for early cavalry.
```

**Corrected English fragment:**

```text
On this note, there's another interesting use for Musketeers in vanilla/Warlords. Try postponing Chemistry and beelining to Military Tradition for early cavalry; in BtS, cavalry also require Rifling, so this early timing no longer applies.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Then research Gunpowder (which is also needed for cavalry)
```

**Corrected English fragment:**

```text
Then research Gunpowder (which, along with Horseback Riding, is also needed for cavalry in vanilla/Warlords)
```

Preserve the older early-Cavalry tactic while identifying the BtS Rifling requirement. Horseback Riding is also a construction prerequisite in the checked original versions.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_CAVALRY/PrereqTech and TechTypes
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-gallic-hill-movement

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
thanks to Guerilla III's movement bonus on hills
```

**Corrected English fragment:**

```text
thanks to Guerilla II's movement bonus on hills
```

Guerrilla II supplies double movement on hills. Guerrilla III supplies the attack/withdrawal bonuses described in the following sentence.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_GUERILLA2/bHillsDoubleMove and PROMOTION_GUERILLA3
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-general-experience-sharing

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Attaching a Great General to a unit gives you 20 XP, so that Jaguar effectively only needs 6 XP,
```

**Corrected English fragment:**

```text
A Great General distributes 20 XP among eligible units on its tile, so if the Jaguar receives all 20, it effectively only needs 6 XP beforehand,
```

The 20 XP are divided among eligible units on the tile. Keep the author’s valid 6+20=26 example, with the condition needed for the Jaguar to receive all the experience.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_GREAT_GENERAL/iLeaderExperience
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::giveExperience; getExperienceNeeded
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-grenadier-versioned-timing

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
it obsoletes too quickly, since Chemistry is effectively only a few techs away.
```

**Corrected English fragment:**

```text
it obsoletes too quickly in vanilla/Warlords, since Chemistry is effectively only a few techs away; in BtS, grenadiers require Military Science.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
If they manage to get to Chemistry, which isn't that far away, this UU is practically obsolete.
```

**Corrected English fragment:**

```text
If they manage to get to Chemistry in Warlords, which isn't that far away, this UU is practically obsolete; in BtS, grenadiers require Military Science.
```

The original chemistry timing is valid in vanilla/Warlords. BtS moves Grenadiers to Military Science. Label the historical argument without replacing the author’s strategy.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_GRENADIER/PrereqTech
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-hurry-resistance

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
in newly conquered cities that are not connected to any metal resource, immediately creating some units
```

**Corrected English fragment:**

```text
in newly conquered cities that are not connected to any metal resource once resistance ends, creating some units
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
rush build Ikhandas in them to help pay
```

**Corrected English fragment:**

```text
rush build Ikhandas in them once resistance ends to help pay
```

canHurry rejects a city in disorder. The no-resource Jaguar and Ikhanda strategies remain useful after occupation resistance ends, but cannot be rushed immediately during resistance.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvCity::canHurry
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-hwacha-combat-limit

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
the inability of siege weapons to kill units and to gain more than 1 experience point per battle.
```

**Corrected English fragment:**

```text
the inability of attacking siege units to kill the defender, with a base award of 1 experience point when an attack reaches the combat limit. Defending siege units can still kill attackers and earn more experience.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
rely on a stack of Hwachas to actually capture cities for you.
```

**Corrected English fragment:**

```text
rely on a stack of Hwachas to defeat the last defenders and capture cities for you, although they can enter an undefended city.
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
Then there's the 1xp only rule, which is worse since it means your Hwachas can no longer gain valuable additional promotions through combat, making it less effective.
```

**Corrected English fragment:**

```text
Then there's the base 1xp award for these attacks, which slows the rate at which your Hwachas gain valuable additional promotions through combat, making them less effective.
```

The BtS attack branch stops at the unit’s combat limit and awards EXPERIENCE_FROM_WITHDRAWL=1 before modifiers. This does not make defence nonlethal, prevent all promotion progress, or set bNoCapture on the unit.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_KOREAN_HWACHA/iCombatLimit and bNoCapture; EXPERIENCE_FROM_WITHDRAWL
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::resolveCombat
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-hwacha-cost-version

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
withdrawal chance for a mere five hammers more (Normal speed).
```

**Corrected English fragment:**

```text
withdrawal chance for a mere five hammers more in Warlords (Normal speed); in BtS it costs fifteen more and its attacks have a nonlethal combat limit.
```

Warlords Hwacha costs 40 against Axeman 35 and has 25% withdrawal. BtS Hwacha costs 50 and its combat limit is 75 instead. Retain the original five-hammer comparison within its valid version.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_KOREAN_HWACHA and UNIT_AXEMAN/iCost, iWithdrawalProb and iCombatLimit
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-immortal-anti-axe

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
chariots don't get the 50% bonus when attacking axemen like in Warlords
```

**Corrected English fragment:**

```text
chariots don't get the 100% bonus when attacking axemen like in Warlords
```

The Warlords/BtS Chariot and Immortal have +100% attack against the Axeman class. Their separate +50% bonus against archery units is unchanged.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_PERSIA_IMMORTAL and UNIT_CHARIOT/UnitClassAttackMods
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-immortal-versioned-withdrawal

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
an innate 30% withdrawal chance.
```

**Corrected English fragment:**

```text
an innate 30% withdrawal chance in vanilla, or 10% in Warlords/BtS.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
a total of 60% withdrawal chance.
```

**Corrected English fragment:**

```text
a total of 60% withdrawal chance in vanilla, or 40% in Warlords/BtS.
```

The original 30/60 figures are valid for vanilla. The expansions reduce the base to 10, so Flanking I+II yield 40. Preserve both historical contexts explicitly.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_PERSIA_IMMORTAL/iWithdrawalProb; FLANKING1 and FLANKING2
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-impi-commando-version

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
If you manage to get it beyond Combat IV, you can add Commando to the collection.
```

**Corrected English fragment:**

```text
Once it has Combat IV, you can add Commando to the collection; in BtS this also requires Military Science.
```

Commando requires Combat IV. BtS additionally requires Military Science, while Warlords does not; this limits the timing of the suggested early Impi gambit.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_COMMANDO/PromotionPrereqOr1 and TechPrereq
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-impi-worker-capture

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
to killl a worker and then getting out
```

**Corrected English fragment:**

```text
to capture a worker and then getting out
```

An ordinary Impi can capture a hostile Worker: its bNoCapture is false and the Worker has a worker capture class. Also remove the typographical triple l as part of the factual correction.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_ZULU_IMPI/bNoCapture and UNIT_WORKER/Capture
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-jaguar-healing

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
the ability to heal units on the same tile at the rate of 15% per turn
```

**Corrected English fragment:**

```text
a +15 percentage-point healing bonus for units on the same tile
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
giving you a whooping 50% healing rate.
```

**Corrected English fragment:**

```text
giving you a whopping +40 percentage-point healing bonus: 50% per turn on ordinary neutral terrain, where the base rate is 10%.
```

Woodsman III adds 15, Medic I adds 10 and Medic III adds 15 to same-tile healing, for +40. A 50% total is correct only with the ordinary neutral-tile base of 10; do not mistake the promotion bonus for the complete healing rate.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: WOODSMAN3, MEDIC1, MEDIC3 and NEUTRAL_HEAL_RATE
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::healRate
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-janissary-tech-path

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
(Maths -> Currency -> Priesthood? -> Civil Service -> Paper -> Education)
```

**Corrected English fragment:**

```text
(Writing -> Code of Laws -> Civil Service -> Paper -> Education, with Mathematics required for Civil Service and either Currency or Priesthood needed for Code of Laws)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
probably research Liberalism first to grab Nationalism as the free tech, before actually researching Gunpowder.
```

**Corrected English fragment:**

```text
probably be the first to research Liberalism (which also requires Philosophy), use its free tech for Nationalism, and adopt Nationhood before actually researching Gunpowder.
```

The northern path omitted Code of Laws and Writing and incorrectly made Currency/Priesthood sequential. Civil Service also needs Mathematics. Liberalism’s free technology belongs to its first discoverer, and drafting requires adopting Nationhood, not merely researching Nationalism.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: TECH_CODE_OF_LAWS, TECH_CIVIL_SERVICE, TECH_LIBERALISM; CIVIC_NATIONHOOD
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-keshik-expansion-scope

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
With barracks and Ger in the city, a Keshik gets 7 xp upon being built.
```

**Corrected English fragment:**

```text
In Warlords/BtS, with barracks and Ger in the city, a Keshik gets 7 xp upon being built. The Ger and the 20% base withdrawal chance used below are expansion features; vanilla Keshiks have no base withdrawal chance.
```

The article shifts between vanilla and Warlords. The Ger exists in the expansions and the Keshik’s base withdrawal changes from 0 to 20. Explicitly scope the ensuing 7/11-XP and 50%-withdrawal example.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: BUILDING_BARRACKS, BUILDING_MONGOL_GER and UNIT_MONGOL_KESHIK
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-machine-gun-collateral

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(which are immune to collateral damage)
```

**Corrected English fragment:**

```text
(which in Warlords/BtS are immune to collateral damage from siege units)
```

The expansion XML grants immunity to the SIEGE combat class, and collateralCombat tests the attacking combat class. This is not immunity to all collateral sources; the checked scope is explicit.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_MACHINE_GUN/UnitCombatCollateralImmunes
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::collateralCombat
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-numidian-flanking

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
whereby it does 'collateral damage' to siege units in the stack it is attacking
```

**Corrected English fragment:**

```text
whereby it does 'collateral damage' to catapults and trebuchets if it survives an attack outside a city (or a fort treated as a city)
```

Numidian flanking targets the listed siege classes, occurs after surviving combat by winning or withdrawing, and is suppressed on plots treated as cities. Preserve the author’s informal collateral-damage analogy.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_CARTHAGE_NUMIDIAN_CAVALRY/FlankingStrikes
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::resolveCombat and CvUnit::flankingStrikeCombat
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-numidian-siege-bonus

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
as well as the 50% bonus vs. siege that horse archers have
```

**Corrected English fragment:**

```text
as well as the horse archer's +50% attack bonus against catapults (and trebuchets in Warlords)
```

The bonus is an attack-only modifier against named unit classes, not a general modifier against all siege units. Warlords lists Catapult and Trebuchet; BtS lists Catapult.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_CARTHAGE_NUMIDIAN_CAVALRY/UnitClassAttackMods
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-obvious-language-errors

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
actually good UU
```

**Corrected English fragment:**

```text
actually a good UU
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
ability to more very quickly
```

**Corrected English fragment:**

```text
ability to move very quickly
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
the Numidian Archer is slightly stronger now
```

**Corrected English fragment:**

```text
the Numidian Cavalry is slightly stronger now
```

**Fragment 4; exact occurrences: 1.**

**Original English fragment:**

```text
scuicide catapults
```

**Corrected English fragment:**

```text
suicide catapults
```

**Fragment 5; exact occurrences: 1.**

**Original English fragment:**

```text
fewer xp points get promoted
```

**Corrected English fragment:**

```text
fewer xp points to get promoted
```

**Fragment 6; exact occurrences: 1.**

**Original English fragment:**

```text
immunity from first strikes are rare enough
```

**Corrected English fragment:**

```text
immunity to first strikes is rare enough
```

**Fragment 7; exact occurrences: 1.**

**Original English fragment:**

```text
up to double the number units in a turn
```

**Corrected English fragment:**

```text
up to double the number of units in a turn
```

**Fragment 8; exact occurrences: 1.**

**Original English fragment:**

```text
too strong be countered well
```

**Corrected English fragment:**

```text
too strong to be countered well
```

**Fragment 9; exact occurrences: 1.**

**Original English fragment:**

```text
the increased number turns needed
```

**Corrected English fragment:**

```text
the increased number of turns needed
```

**Fragment 10; exact occurrences: 1.**

**Original English fragment:**

```text
Hwachas, being super catapults, puts
```

**Corrected English fragment:**

```text
Hwachas, being super catapults, put
```

**Fragment 11; exact occurrences: 1.**

**Original English fragment:**

```text
After you several of them
```

**Corrected English fragment:**

```text
After you have several of them
```

**Fragment 12; exact occurrences: 2.**

**Original English fragment:**

```text
becareful
```

**Corrected English fragment:**

```text
be careful
```

**Fragment 13; exact occurrences: 1.**

**Original English fragment:**

```text
the only hope Mongolian player might have
```

**Corrected English fragment:**

```text
the only hope a Mongolian player might have
```

**Fragment 14; exact occurrences: 1.**

**Original English fragment:**

```text
planning a large-scale settling another landmass
```

**Corrected English fragment:**

```text
planning a large-scale settlement of another landmass
```

**Fragment 15; exact occurrences: 1.**

**Original English fragment:**

```text
accumulated much EPs
```

**Corrected English fragment:**

```text
accumulated many EPs
```

**Fragment 16; exact occurrences: 1.**

**Original English fragment:**

```text
and rapidly exploiting this opportunity gap
```

**Corrected English fragment:**

```text
and rapidly exploit this opportunity gap
```

**Fragment 17; exact occurrences: 1.**

**Original English fragment:**

```text
Jannissaries
```

**Corrected English fragment:**

```text
Janissaries
```

**Fragment 18; exact occurrences: 1.**

**Original English fragment:**

```text
You may end up too many cities
```

**Corrected English fragment:**

```text
You may end up with too many cities
```

**Fragment 19; exact occurrences: 1.**

**Original English fragment:**

```text
you should have great time conquering
```

**Corrected English fragment:**

```text
you should have a great time conquering
```

Correct unambiguous spelling, omitted words, subject–verb agreement and one incorrect unit name. Keep the author’s humour, strategic opinions, register, section order and argumentation.

**Verification:**

- `Assets/XML/Text/STRATEGIES_PEDIA.xml`; TXT_KEY_STRATEGY_UU_PEDIA/English
  SHA-256: `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`.
  Direct inspection of the English wording; no gameplay claim introduced.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-oromo-draft-xp

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
you can get Drill III draftees with just Theocracy/Vassalage/a military instructor.
```

**Corrected English fragment:**

```text
you can get Drill III draftees with barracks plus either Theocracy (with the state religion in the city) or a military instructor. Drafting halves the XP; Vassalage cannot be combined with Nationhood.
```

Draft XP is integer-divided by 2. Two XP from Theocracy or an instructor alone becomes one, below the two-XP promotion threshold; Barracks 3 plus the extra 2 gives (3+2)//2=2. Vassalage and Nationhood occupy the same civic category.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: BUILDING_BARRACKS; CIVIC_THEOCRACY, CIVIC_VASSALAGE and CIVIC_NATIONHOOD
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvCity::getProductionExperience and CvCity::addProductionExperience
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-panzer-barrage-version

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
having access to both Barrage and City Raider promotions.
```

**Corrected English fragment:**

```text
having access to both Barrage and City Raider promotions in vanilla/Warlords; BtS 3.19 removes Barrage from armour units.
```

The base-game and Warlords Barrage promotion allows ARMOR, but the installed original BtS 3.19 XML does not. Preserve the valid older advice and label the difference.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_BARRAGE1/UnitCombats
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-phalanx-chariot-modifiers

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
That means chariots do not get a 100% bonus when attacking them.
```

**Corrected English fragment:**

```text
Chariots still get their +100% attack bonus against the axeman class, but the Phalanx counters it with its own +100% defence bonus against chariots.
```

BtS retains the Chariot’s class attack bonus and gives the Phalanx an opposing class defence bonus. The result is not implemented by removing the attacker’s bonus.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_CHARIOT/UnitClassAttackMods and UNIT_GREEK_PHALANX/UnitClassDefenseMods
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-redcoat-vanilla-version

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
The terror of your enemies in Civ4 vanilla, this unit is dramatically different in Warlords.
```

**Corrected English fragment:**

```text
The terror of your enemies in Civ4 vanilla 1.61, this unit is dramatically different in vanilla 1.74 and the expansions.
```

The actual 1.61 patch UnitInfos has strength 16; installed vanilla 1.74, Warlords 2.13 and BtS 3.19 have strength 14. Preserve the historical statistic instead of silently replacing it, and avoid implying the change was exclusive to Warlords.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: UNIT_ENGLISH_REDCOAT/iCombat in all four versions
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; historical_patch_provenance
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-seal-amphibious-river

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
amphibious attacks (which include those across a river, by the way)
```

**Corrected English fragment:**

```text
amphibious attacks (the Amphibious promotion also removes the river-crossing attack penalty, by the way)
```

A river attack is not an amphibious landing, although the same Amphibious promotion removes both penalties.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: river combat modifier; primary_xml: PROMOTION_AMPHIBIOUS/bAmphib
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-seal-healing

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Bringing a Medic III unit along with your SEALs means
```

**Corrected English fragment:**

```text
In Warlords/BtS, bringing a Medic III unit along with your SEALs on an ordinary enemy tile means
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
They can also heal right after making an amphibious assault aboard a Medic transport.
```

**Corrected English fragment:**

```text
They can also heal at the next healing step after an amphibious assault if they remain aboard the Medic transport on the same tile; its adjacent-tile healing does not cross from a water area to a land area.
```

Medic III is an expansion promotion; Medic I plus III contributes 25 healing points and an ordinary enemy tile contributes 5. March allows the normal doTurn healing after moving, not immediate healing during combat. Adjacent-tile healing requires the same area, unlike same-tile healing.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: PROMOTION_MEDIC1 and PROMOTION_MEDIC3
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: ENEMY_HEAL_RATE
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: CvUnit::healRate and CvUnit::doTurn
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### uu-stable-barracks-xp

- **Tag:** `TXT_KEY_STRATEGY_UU_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
If you're playing on Warlords, stables can give your Camel Archers enough experience points to start off with Flanking I and II
```

**Corrected English fragment:**

```text
If you're playing on Warlords, barracks plus stables give your Camel Archers enough experience points to start off with Flanking I and II
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
so, with stables, you can give them Flanking II and another promotion
```

**Corrected English fragment:**

```text
so, with barracks and stables, you can give them Flanking II and another promotion
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
just be sure to build stables and give them Combat I and Shock
```

**Corrected English fragment:**

```text
just be sure to build barracks and stables and give them Combat I and Shock
```

A Stable alone contributes 2 XP. Barracks contribute 3 in both expansions, so together they meet the 5-XP threshold for two selected promotions. A free Numidian Flanking I does not supply the missing XP.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; primary_xml: BUILDING_BARRACKS and BUILDING_STABLE
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/uu-primary-verification.json`; sdk: Warlords CvUnit::experienceNeeded; BtS getExperienceNeeded
  Audit snapshot SHA-256: `842575fe46ed17561c57894bbb5361101e760b4d661990caf911016cdf89db23`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-complaints

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
General Compaints
```

**Corrected English fragment:**

```text
General Complaints
```

Correct the misspelled heading; preserve its wording and emphasis.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-financial-threshold

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Financial (+1 Commerce on 2 Commerce plots)
```

**Corrected English fragment:**

```text
Financial (+1 Commerce on plots already producing at least 2 Commerce)
```

The Financial threshold is a minimum: tiles already producing 2 or more commerce qualify. This preserves the historical Warlords rule.

**Verification:**

- `Warlords/Assets/XML/Civilizations/CIV4TraitInfos.xml`; TRAIT_ORGANIZED/iUpkeepModifier=-50; TRAIT_FINANCIAL/ExtraYieldThresholds=(0,0,2)
  SHA-256: `ede6147100a39ff2d0bd226ff3c92cb4ac613ba9049d7713cdd325c355a7f34d`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-grateful

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
gratefull
```

**Corrected English fragment:**

```text
grateful
```

Grateful has one final l.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-greater-than

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
significantly greater then,
```

**Corrected English fragment:**

```text
significantly greater than,
```

The comparison requires than; then expresses time.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-loses

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
looses
```

**Corrected English fragment:**

```text
loses
```

Lose (loses) means to cease to possess; loose is a different verb. All three occurrences describe lost cities or territory.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-many-games

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
a great great many game will end
```

**Corrected English fragment:**

```text
a great great many games will end
```

Many requires the plural games; the author’s emphatic repetition is retained.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-masters-population

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Maters Population
```

**Corrected English fragment:**

```text
Master's Population
```

Correct the misspelled possessive reference to the master civilization.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-missing-be

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
There may good short term advantages
```

**Corrected English fragment:**

```text
There may be good short term advantages
```

Restore the missing verb after may.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-newly-acquired

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
newly acquire cities
```

**Corrected English fragment:**

```text
newly acquired cities
```

Use the past participle to describe cities that have been acquired.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-organized-upkeep

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Organized (-50% Empire Maintenance)
```

**Corrected English fragment:**

```text
Organized (-50% Civic Upkeep)
```

Organized reduces civic upkeep, not all empire maintenance. The historical Warlords trait and CvPlayer upkeep calculation agree.

**Verification:**

- `Warlords/Assets/XML/Civilizations/CIV4TraitInfos.xml`; TRAIT_ORGANIZED/iUpkeepModifier=-50; TRAIT_FINANCIAL/ExtraYieldThresholds=(0,0,2)
  SHA-256: `ede6147100a39ff2d0bd226ff3c92cb4ac613ba9049d7713cdd325c355a7f34d`.
- `Warlords/CvGameCoreDLL/CvPlayer.cpp`; CvPlayer::getSingleCivicUpkeep applies getUpkeepModifier to civic upkeep.
  SHA-256: `fea8c8e91a69988855fdbca0eb8ecc544458b53b70b1a68a209257ef6e80abef`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-outstanding

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Outsanding Questions
```

**Corrected English fragment:**

```text
Outstanding Questions
```

Correct the misspelled heading.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-peaceful-strategies

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
encourage peacefully strategies
```

**Corrected English fragment:**

```text
encourage peaceful strategies
```

An adjective, peaceful, modifies the noun strategies.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-possessive-its

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
sacrificing it's independence
```

**Corrected English fragment:**

```text
sacrificing its independence
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
half of it's territory
```

**Corrected English fragment:**

```text
half of its territory
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
lose it's strategic value
```

**Corrected English fragment:**

```text
lose its strategic value
```

**Fragment 4; exact occurrences: 1.**

**Original English fragment:**

```text
lowering it's discretionary spending
```

**Corrected English fragment:**

```text
lowering its discretionary spending
```

**Fragment 5; exact occurrences: 1.**

**Original English fragment:**

```text
all of it's territory
```

**Corrected English fragment:**

```text
all of its territory
```

**Fragment 6; exact occurrences: 1.**

**Original English fragment:**

```text
and it's client states
```

**Corrected English fragment:**

```text
and its client states
```

**Fragment 7; exact occurrences: 1.**

**Original English fragment:**

```text
expansion of it's own
```

**Corrected English fragment:**

```text
expansion of its own
```

**Fragment 8; exact occurrences: 1.**

**Original English fragment:**

```text
against it's rival Civ groupings
```

**Corrected English fragment:**

```text
against its rival Civ groupings
```

These eight phrases use the possessive determiner its, not the contraction it's (it is/it has).

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-razed

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
cities are getting raised or captured
```

**Corrected English fragment:**

```text
cities are getting razed or captured
```

The context is destruction of cities, which is razing, not raising.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-score-percentage

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
10.5pts (+16%)
```

**Corrected English fragment:**

```text
10.5pts (+16.7%)
```

In the author’s explicitly simplified point model, the increase is (10.5−9)/9×100=16⅔%, or 16.7% to one decimal place. The table and model are retained.

**Verification:**

- `Explicit calculation`
  (10.5 - 9) / 9 * 100 = 50/3 = 16.666666...

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-too-shabby

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Not to shabby
```

**Corrected English fragment:**

```text
Not too shabby
```

The intensifier is too, not the preposition to.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### vassal-your-relations

- **Tag:** `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
in you relations
```

**Corrected English fragment:**

```text
in your relations
```

The noun relations requires the possessive determiner your in this phrase.

**Verification:**

- `Explicit calculation`
  Direct inspection of the quoted phrase in the complete original English article; no mechanical claim changed.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### war-ai-modifier-scope

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
x AIs Modifier (100% at Settler..10% lower for each level up)
```

**Corrected English fragment:**

```text
x AIs Modifier (AI players only: 100% at Settler..10% lower for each level up)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
x (100+AI Per Era Modifier * Era)% [-1 for every Level above Noble]
```

**Corrected English fragment:**

```text
x (100+AI Per Era Modifier * Era)% [AI players only; -1 for every Level above Noble]
```

Difficulty and era discounts are applied only inside the non-human, non-barbarian branch. Human players must not apply these two factors.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/additional-sdk-evidence.json`; CvPlayer::updateWarWearinessPercentAnger non-human branch
  Audit snapshot SHA-256: `dfc635c7e49ae05a424d8860596729ec1bf9018a90fbdde540766e64ce88a580`.

**Compatibility:** Explicit vanilla 1.61 scope.

### war-combat-event-values

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Your unit attacks their unit=+3 if you lose, +1 if you win
```

**Corrected English fragment:**

```text
Your unit attacks their unit=+3 if you lose, +2 if you win
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Their unit attacks your unit =+2 (win or lose)
```

**Corrected English fragment:**

```text
Their unit attacks your unit =+2 if you lose, +1 if you win
```

Vanilla 1.61 defines attacker victory as +2 and defender victory as +1, subject to the article's cultural-territory conditions. The original swaps these event values.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/war-weariness-evidence.json`; CvUnit.cpp attack/death event branches and GlobalDefines WW constants
  Audit snapshot SHA-256: `d0d9856fc6c9f78a805b765e34624ce3896a28d1efeae10253d3db8ff63b7e73`.

**Compatibility:** Explicitly vanilla 1.61, not Warlords or later mods.

### war-formula-rounding-scope

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
So the "simple" [BOLD]formula[\BOLD] seems to be:
```

**Corrected English fragment:**

```text
So the "simple" [BOLD]formula[\BOLD] below is an approximation before the game truncates intermediate integer calculations and combines anger into unhappy citizens:
```

The displayed product is a conceptual approximation. The SDK truncates integer stages before computing city anger, so a single real-valued product is not an exact count of unhappy citizens.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/additional-sdk-evidence.json`; CvPlayer::updateWarWearinessPercentAnger successive integer division
  Audit snapshot SHA-256: `dfc635c7e49ae05a424d8860596729ec1bf9018a90fbdde540766e64ce88a580`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/war-weariness-evidence.json`; BASE_WAR_WEARINESS_MULTIPLIER and PERCENT_ANGER_DIVISOR
  Audit snapshot SHA-256: `d0d9856fc6c9f78a805b765e34624ce3896a28d1efeae10253d3db8ff63b7e73`.

**Compatibility:** Explicit vanilla 1.61 scope.

### war-nuke-per-team

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
You launch a nuke=+12 (WW regardless of culture)
```

**Corrected English fragment:**

```text
You launch a nuke=+12 against each affected team (WW regardless of culture)
```

The nuclear loop adds twelve war-weariness points against each affected team, not twelve total across all targets.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/additional-sdk-evidence.json`; CvUnit.cpp WW_ATTACKED_WITH_NUKE inside abTeamsAffected loop
  Audit snapshot SHA-256: `dfc635c7e49ae05a424d8860596729ec1bf9018a90fbdde540766e64ce88a580`.

**Compatibility:** Explicit vanilla 1.61 scope.

### war-peace-decay-example-scope

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Each turn =-1
```

**Corrected English fragment:**

```text
Each turn =-1 while WW is above zero
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Because making peace for the 10 turns can take ~20 points off
```

**Corrected English fragment:**

```text
Around the example's starting value of 102 WW, making peace for 10 turns can remove about 20 raw points
```

Ten peaceful turns do not remove a universal twenty points. In the article's own starting example, 102 becomes 81 after ten sequential minus-one and 99%-floor steps, so about twenty is appropriate only around that starting amount.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/additional-sdk-evidence.json`; CvTeam::doWarWeariness
  Audit snapshot SHA-256: `dfc635c7e49ae05a424d8860596729ec1bf9018a90fbdde540766e64ce88a580`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; war_peace_decay
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Explicit vanilla 1.61 peace decay; historical example retained.

### war-standard-map-percent

- **Tag:** `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Basically with no Modifiers on a standard map:
```

**Corrected English fragment:**

```text
On a Standard map with no other modifiers:
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Every "Foreign" City you take= 3% WW
```

**Corrected English fragment:**

```text
Every "Foreign" City you take adds 2.7 percentage points of WW anger
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
=~10% Anger reduction when you restart the War.
```

**Corrected English fragment:**

```text
=~9 percentage points of anger reduction on a Standard map with no other modifiers when you restart the War.
```

Standard map uses a 90% WW multiplier. A captured city contributes 6/200*0.9=2.7 percentage points; removing twenty raw WW points reduces anger by nine percentage points under the same assumptions.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; WORLDSIZE_STANDARD iWarWearinessModifier=-10
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; standard_map_war_weariness
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Explicitly vanilla 1.61, Standard map, no other modifiers; using the article's approximate percentage model.

### health-bold-close

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
[BOLD]Note that there are ways to reduce unhealthiness:[BOLD]
```

**Corrected English fragment:**

```text
[BOLD]Note that there are ways to reduce unhealthiness:[\BOLD]
```

The second BOLD opener must be a closing tag. This is an explicit, localized formatting-token repair.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/source-manifest.json`; Group 13040 unclosed Note heading
  Audit snapshot SHA-256: `14a15b68c64cefbf2c2d50280fb8ac3d04e5ea58a9084d98a080d999f3bdbca3`.

**Compatibility:** Civilopedia text markup.

### health-building-total

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
You can have a total of +21 health from buildings, 16 of those being already accounted for in chapter 1: the resources.
```

**Corrected English fragment:**

```text
You can have a total of +19 health from the listed buildings, 14 of those being already accounted for in chapter 1: the resources.
```

The listed buildings supply 2+3 unconditional health and 3+4+3+4 resource-dependent health, totaling nineteen, fourteen of which is resource dependent.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; Aqueduct, Hospital, Granary, Grocer, Harbor, Supermarket
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; health_building_totals
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Historical vanilla buildings enumerated in this article; not the larger mod building roster.

### health-equality

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
As long as you have more healthiness than unhealthiness, you have no
```

**Corrected English fragment:**

```text
As long as healthiness is at least equal to unhealthiness, you have no
```

Health equal to unhealthiness already prevents food loss; a strictly positive surplus is unnecessary.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; CvCity::healthRate in both inspected SDK versions
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.

**Compatibility:** Vanilla 1.61 and installed BtS SDK healthRate.

### health-grocer-techs

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 2.**

**Original English fragment:**

```text
with grocer (requires [BOLD]Guild[\BOLD])
```

**Corrected English fragment:**

```text
with grocer (requires [BOLD]Guilds and Currency[\BOLD])
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
requires [BOLD]guilds[\BOLD];
```

**Corrected English fragment:**

```text
requires [BOLD]guilds and currency[\BOLD];
```

Grocer requires both Guilds and Currency. Guilds alone does not imply Currency through the tech tree.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; BUILDING_GROCER PrereqTech and TechTypes; TECH_GUILDS prerequisites
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.

**Compatibility:** Vanilla 1.61 Grocer prerequisites.

### health-missing-sheep

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(Banana; Clam; Corn; Cow; Crab; Deer; Fish; Pig; Rice; Wheat)
```

**Corrected English fragment:**

```text
(Banana; Clam; Corn; Cow; Crab; Deer; Fish; Pig; Rice; Sheep; Wheat)
```

The overview list omits Sheep even though the detailed resource list includes it and XML grants one health.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/xml-evidence.json`; BONUS_SHEEP iHealth=1
  Audit snapshot SHA-256: `8b298de3f45146736f73be66a6fedf6d26500e5f7c8406cbfa5b6e8107acc97b`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/source-manifest.json`; Group 13040 later Sheep entry
  Audit snapshot SHA-256: `14a15b68c64cefbf2c2d50280fb8ac3d04e5ea58a9084d98a080d999f3bdbca3`.

**Compatibility:** Historical vanilla health-resource list.

### health-recycling-dirty-power

- **Tag:** `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Building a recycling centre removes building unhealthiness.
```

**Corrected English fragment:**

```text
Building a recycling centre removes direct building unhealthiness, but not the separate unhealthiness from dirty power.
```

Recycling removes direct building unhealthiness via the building-only-healthy flag. Dirty-power health is tracked and added separately, so it remains.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/additional-sdk-evidence.json`; CvCity::totalBadBuildingHealth and CvCity::updatePowerHealth
  Audit snapshot SHA-256: `dfc635c7e49ae05a424d8860596729ec1bf9018a90fbdde540766e64ce88a580`.

**Compatibility:** Vanilla 1.61 SDK; historical health article.

### production-ap-religion-and-membership

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
(the state religion of the Apostolic Palace owner)
```

**Corrected English fragment:**

```text
(the builder's state religion when the Apostolic Palace was completed)
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
In a similar fashion, you can get 2H per religious building of the Apostolic's Palace religion if you run it as state religion.
```

**Corrected English fragment:**

```text
In a similar fashion, eligible buildings of the Apostolic Palace's religion provide 2H while the Palace is active and you are a loyal member. That religion does not have to be your current state religion.
```

The Palace religion is assigned from the builder's state religion when first completed and is not updated from its current owner's religion. Religious-building yields depend on the active vote source and loyal membership, not adopting that religion as current state religion.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-sdk-evidence.json`; setVoteSourceReligion call in CvCity::setNumRealBuilding; CvCity::processVoteSourceBonus; CvPlayer::setLoyalMember
  Audit snapshot SHA-256: `1eaa07f0020725be83160790ebe188e5e890d44ac9f074493c08136cb828538a`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; DIPLOVOTE_POPE ReligionYields=0,2,0
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Beyond the Sword only.

### production-cash-rush-modifier-scope

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Bonuses don't apply.
```

**Corrected English fragment:**

```text
Production bonuses do not reduce the gold price; separate hurry-cost modifiers still apply.
```

Hammer-production bonuses do not lower the gold price. Separate hurry-cost modifiers still apply, so the unqualified claim that bonuses do not apply is too broad.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; CvCity::hurryGold and CvCity::hurryCost
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.

**Compatibility:** Vanilla 1.61 and installed BtS hurry cost paths.

### production-cash-rush-overflow-example

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
What do you get? you get the item at the end of your turn, there is an overflow of exactly your base hammers.
```

**Corrected English fragment:**

```text
What do you get? You get the item at the end of your turn. The turn's ordinary production becomes overflow, subject to the overflow cap, normalization by the current production modifier, and integer rounding.
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
turn 9: you can build what you want with (20 hammers overflow + 5 base hammers )*1,25 from the forge = 31 hammers.
```

**Corrected English fragment:**

```text
turn 9: the stored base overflow after turns 5, 6, 7 and 8 is 4, 8, 12 and 16 hammers respectively. You can build what you want with FLOOR((16 hammers overflow + 5 base hammers)*1.25 from the forge) = 26 hammers.
```

**Fragment 3; exact occurrences: 1.**

**Original English fragment:**

```text
Now try it with your massive base hammers city, and get a 4 turns discount on the engine production.
```

**Corrected English fragment:**

```text
Now try it with your massive base hammers city to carry production from four turns into the engine. The number of turns saved depends on its production modifiers and rounding.
```

Completed buildings activate before overflow normalization. Completing the Forge normalizes the first five excess hammers to four base overflow; subsequent integer normalization gives 8, 12 and 16. The final turn yields 26, not 31. Overflow is subject to caps and modifiers, so an unconditional four-turn discount is also unjustified.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; CvCity::popOrder building completion before changeOverflowProduction; getProductionDifference; changeOverflowProduction
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; cash_rush_overflow_example
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** The article's Forge-first cash-rush example, verified against vanilla 1.61 and installed BtS SDK sequencing. No overflow cap binds in this example.

### production-catapult-version-scope

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `VERSION_SPECIFIC`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Turn 1 : you assign all your citizens to max food tiles, earning a few "normal" hammers (let's say 3), and start producing an item (let's say a catapult)
```

**Corrected English fragment:**

```text
This example uses the 40-hammer Catapult from vanilla/Warlords; the BtS Catapult costs 50, so its corresponding overflow and next-turn totals would be 16 and 19.[NEWLINE]Turn 1 : you assign all your citizens to max food tiles, earning a few "normal" hammers (let's say 3), and start producing an item (let's say a catapult)
```

The 26-hammer overflow and 29-hammer next turn are correct for the forty-hammer vanilla/Warlords Catapult. BtS has a fifty-hammer Catapult, yielding sixteen and nineteen under the same assumptions. Preserve the historical example with explicit scope.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; UNIT_CATAPULT costs40 in vanilla/Warlords and50 in BtS
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Vanilla/Warlords numerical example; BtS distinction only.

### production-civic-bonus-conditions

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
police state, +25% for units
```

**Corrected English fragment:**

```text
police state, +25% for military units
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
organized religion, +25% for buildings (includes wonders, but not space parts)
```

**Corrected English fragment:**

```text
organized religion, +25% for buildings in cities with your state religion (includes wonders, but not space parts)
```

Police State applies to military units. Organized Religion's building bonus requires the player's state religion in the city.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; CIVIC_POLICE_STATE iMilitaryProductionModifier=25; CIVIC_ORGANIZED_RELIGION iStateReligionBuildingProductionModifier=25
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-sdk-evidence.json`; CvCity::getProductionModifier overloads: military flag and state religion present in city
  Audit snapshot SHA-256: `1eaa07f0020725be83160790ebe188e5e890d44ac9f074493c08136cb828538a`.

**Compatibility:** Historical vanilla/Warlords/BtS civic scope.

### production-copper-projects

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
copper +100% to Buddhist Stupas, Confucian Academies, Taoist Pagodas, to space parts (Cockpit, Life Support, Stasis Chamber) and a few wonders including the Internet
```

**Corrected English fragment:**

```text
copper +100% to Buddhist Stupas, Confucian Academies, Taoist Pagodas, to space parts (Cockpit and Life Support), to the Internet project and to a few wonders; the Stasis Chamber has no copper production bonus
```

Copper accelerates Cockpit and Life Support but not Stasis Chamber. The Internet is a project, not a wonder.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; PROJECT_SS_COCKPIT, PROJECT_SS_LIFE_SUPPORT, PROJECT_SS_STASIS_CHAMBER, PROJECT_THE_INTERNET BonusProductionModifiers
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Vanilla/Warlords/BtS project definitions.

### production-fractional-hammers

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
10 * (1+0,25 from orgrel + 0,5 from capital + 0,5 from industrious) = 22,5 hammers/turn.
```

**Corrected English fragment:**

```text
10 * (1+0,25 from orgrel + 0,5 from capital + 0,5 from industrious) = 22,5 nominal hammers/turn, rounded down to 22 actual hammers/turn.
```

The nominal 22.5 yield is truncated to 22 actual production by the integer production calculation.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/sdk-evidence.json`; CvCity::getProductionDifference in both inspected SDK versions
  Audit snapshot SHA-256: `baa795ed6a10db235d784bcf8ba3273243e2cbfa2721fcdff1baa51010a1caf5`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/calculations.json`; production_integer_rounding
  Audit snapshot SHA-256: `02e71f9e34ab22bba3680ccd81a62b8d94c37616dd2d71e1ec18a9a5253edc17`.

**Compatibility:** Vanilla 1.61 and installed BtS SDK; same illustrative modifiers.

### production-ger-mounted-scope

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
but with a ger you can reach level 4 out of barracks.
```

**Corrected English fragment:**

```text
but with a ger your mounted units can reach level 4 out of barracks.
```

Ger supplies its extra experience only to mounted units, so the level-four example must specify that unit category.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; BUILDING_MONGOL_GER UnitCombatFreeExperiences UNITCOMBAT_MOUNTED=4
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Warlords and BtS Ger.

### production-industrious-name

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `FACTUAL_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
industrialism also gives a 50% bonus on all wonders,
```

**Corrected English fragment:**

```text
the Industrious trait also gives a 50% bonus on all wonders,
```

The +50% wonder production bonus belongs to the Industrious leader trait, not the Industrialism technology.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; TRAIT_INDUSTRIOUS wonder production modifiers=50
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Historical vanilla/Warlords/BtS trait naming.

### production-irrigated-farm-assumption

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Replaceable Parts to build lumbermills[\BOLD]
```

**Corrected English fragment:**

```text
Replaceable Parts to build lumbermills. The farm yields shown assume irrigation[\BOLD]
```

The displayed farm food yields include the irrigation bonus. State that assumption because Biology permits non-irrigated farms with lower yields.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; IMPROVEMENT_FARM IrrigatedYieldChange and Biology TechYieldChanges
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Historical vanilla/Warlords/BtS terrain examples.

### production-railroad-resources

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(you must have the following techs: guilds, chemistry, replaceable parts, biology (for farms), railroad, you also need iron and coal)
```

**Corrected English fragment:**

```text
(you must have the following techs: guilds, chemistry, replaceable parts, biology (for farms), railroad; building railroads requires coal in vanilla/Warlords, or coal or oil in BtS, but does not require iron)
```

Railroad construction needs Coal in vanilla/Warlords or Coal or Oil in BtS. Iron is not a route prerequisite.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; Full ROUTE_RAILROAD records: vanilla BonusType=BONUS_COAL; BtS BonusType=NONE and PrereqOrBonuses COAL/OIL
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Edition-specific railroad construction requirements; the table's other technology assumptions are preserved.

### production-replaceable-parts-watermills

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Replaceable Parts improves windmills (+1H)
```

**Corrected English fragment:**

```text
Replaceable Parts improves windmills and watermills (+1H)
```

Replaceable Parts adds one production to watermills as well as windmills.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; IMPROVEMENT_WATERMILL and IMPROVEMENT_WINDMILL TechYieldChanges
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.

**Compatibility:** Historical vanilla/Warlords/BtS XML.

### production-whip-minimum-population

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
necessary population = twice the cost of the whip.
```

**Corrected English fragment:**

```text
necessary population: at least twice the population cost of the whip.
```

The rule is population at least twice the population cost, because maxHurryPopulation is floor(population/2). Equality is sufficient but not required.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-sdk-evidence.json`; CvCity::maxHurryPopulation and CvCity::canHurry
  Audit snapshot SHA-256: `1eaa07f0020725be83160790ebe188e5e890d44ac9f074493c08136cb828538a`.

**Compatibility:** Vanilla 1.61 and installed BtS SDK.

### production-yield-table-labels

- **Tag:** `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `LANGUAGE_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
Plains farm: 3F1P
```

**Corrected English fragment:**

```text
Plains farm: 3F1H
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
Plains lumbermill hill: 0F5H
```

**Corrected English fragment:**

```text
Plains lumbermill hill with railroad: 0F5H
```

Use the article's H abbreviation for production and explicitly label the railroad assumed by the five-hammer lumbermill hill.

**Verification:**

- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/production-xml-evidence.json`; Lumbermill route production; Plains and hill yield components
  Audit snapshot SHA-256: `dc947c452eb5ee8a6df7c4c6123be954b67708690e6d6dc8ed6632ad55fee8c4`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-mechanics/source-manifest.json`; Group 13042 same table explicitly labels other railroad improvements
  Audit snapshot SHA-256: `14a15b68c64cefbf2c2d50280fb8ac3d04e5ea58a9084d98a080d999f3bdbca3`.

**Compatibility:** Historical yield-table notation; no numerical modernization.

### wk-artist-culture-range

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Great artists produce +12 to +15 culture per turn
```

**Corrected English fragment:**

```text
Settled great artists produce +12 culture per turn, or +14 with the Sistine Chapel
```

The base specialist contributes 12 culture and the Sistine bonus contributes 2, giving 14 rather than 15. The existing following sentence already separates city culture multipliers from these base outputs.

**Verification:**

- `CIV4BuildingInfos.xml`
  SHA-256: `53bfcb06e4bf29e15e7ca503732b4199a5fb8ea9760216ba3f3d5e0289e83d3d`.
- `CIV4SpecialistInfos.xml`
  SHA-256: `49ff17b45392cc71687513f951b544f65d3692bb2707f40ce4598800a49f51ab`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-city-raider-total

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
receives a +85% bonus against cities
```

**Corrected English fragment:**

```text
receives a +75% bonus against cities, plus a further +10% against gunpowder defenders from City Raider III
```

The three city-attack bonuses total 20+25+30=75. City Raider III adds another 10 only against gunpowder units; 85 is not the unconditional city bonus.

**Verification:**

- `CIV4PromotionInfos.xml`
  SHA-256: `a92f5d59ecbef85bcb5019fb5dd2a11fb01c13275a3a3bfc9feb31522699a489`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-cumulative-gp-costs

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
(5 GPs = 1,500 points, 10 GPs = 5,500 points, 15 GPs = 12,000 points, 20 GPs = 21,000 points, 25 GPs = 32,500 points, 30 GPs = 46,500 points, 35 GPs = 62,000 points, 40 GPs = 82,000 points)
```

**Corrected English fragment:**

```text
(for births that increase the threshold in original Civilization IV 1.61, on Normal speed with an Ancient start and a one-player team: 5 GPs = 1,500 points, 10 GPs = 5,500 points, 15 GPs = 13,500 points, 20 GPs = 26,500 points, 25 GPs = 46,000 points, 30 GPs = 73,000 points, 35 GPs = 109,000 points, 40 GPs = 155,000 points)
```

The source continues a fixed 100-point increase after the tenth birth. CvCity::createGreatPeople increases the increment after every ten births; the one-player team receives both 50-point modifiers. Independent integer calculation gives the corrected cumulative table. State the scenario explicitly rather than applying later mod rules.

**Verification:**

- `Original Civilization IV 1.61 SDK: CvGameCoreDLL_v161/CvGameCoreDLL/CvCity.cpp`; void CvCity::createGreatPeople(
  SHA-256: `b5eb960e558bd70e40928d791dbdd097c9faaad64a09a6c4d756b83ab836ce9e`.
- `Original Civilization IV 1.61 SDK: CvGameCoreDLL_v161/CvGameCoreDLL/CvPlayer.cpp`; int CvPlayer::greatPeopleThreshold()
  SHA-256: `7ce093ee3e13cda6cc64ece3d8e1932481ec77bf9d09e6388fbcf0ab72035c1c`.
- [Evidence register](docs/EVIDENCE-v0.3.json), report `english-v03-content/wk-primary-verification.json`; math.gp_cumulative_table; math.gp_conditions
  Audit snapshot SHA-256: `4087cab3ab72f5ddc0338087872a68660273fa9054d17975d4fe1b947cb80402`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-first-settler-difference

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
first settler 9 turn earlier
```

**Corrected English fragment:**

```text
first settler 8 turns earlier
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
as the 9 turns allow
```

**Corrected English fragment:**

```text
as the 8 turns allow
```

The source table gives turns 25 and 33 for the first settlers, a difference of 8 turns, not 9.

**Verification:**

- `Explicit calculation`
  33-25=8

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-gp-bonus-vs-total

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
Philosophical + Pacifism + Parthenon = 250% great people points, with 350% in the city with the national epic.
```

**Corrected English fragment:**

```text
Philosophical + Pacifism + Parthenon = +250% great people points, with +350% in the city with the national epic, provided the city has your state religion. These bonuses are added to the base rate.
```

The modifiers are bonuses above the base 100% rate. Pacifism contributes its modifier only in cities containing the state religion. CvCity::getTotalGreatPeopleRateModifier adds 100 after summing the modifiers.

**Verification:**

- `Original Civilization IV 1.61 SDK: CvGameCoreDLL_v161/CvGameCoreDLL/CvCity.cpp`; int CvCity::getTotalGreatPeopleRateModifier()
  SHA-256: `b5eb960e558bd70e40928d791dbdd097c9faaad64a09a6c4d756b83ab836ce9e`.
- `CIV4BuildingInfos.xml`
  SHA-256: `53bfcb06e4bf29e15e7ca503732b4199a5fb8ea9760216ba3f3d5e0289e83d3d`.
- `CIV4CivicInfos.xml`
  SHA-256: `60b758e9093e467a24634ded7bfc6ff22e44235e9ed79ebae8ed06fc2c23078a`.
- `CIV4TraitInfos.xml`
  SHA-256: `430bf575e7f371c28b7d5a80c02b2ff32bb358e34d625515d2883cc182d7af7c`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-resource-yield-model

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
irrigate 2 flood plains up to +4 food each
```

**Corrected English fragment:**

```text
irrigate 2 flood plains to 4 food each
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
one special resource you can get 2 food or hammers from
```

**Corrected English fragment:**

```text
one special resource yielding 5 food and hammers in total
```

The stated surplus of 10 requires the resource tile to yield 5 in total: city centre 3 + two floodplains at 4 + resource tile 5 − food consumption 6 = 10. A tile yielding only 2 would give a surplus of 7. Clarify that the floodplain value is its total yield, not an added +4 bonus.

**Verification:**

- `Explicit calculation`
  3+2*4+5-3*2=10; using a resource yield of 2 gives 7
  Repairs the hypothetical numerical example without asserting a particular map resource.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-settled-artist-yields

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MECHANICS_ERROR`
- **Mod version:** 1.3.3

**Original English fragment:**

```text
great people (+3 commerce, +14 culture)
```

**Corrected English fragment:**

```text
great people (+3 gold and +12 culture, or +14 culture with the Sistine Chapel)
```

The settled Great Artist supplies 3 gold and 12 culture as base outputs; the Sistine Chapel adds 2 culture per specialist. The source incorrectly calls the gold commerce and leaves the Sistine condition unstated.

**Verification:**

- `CIV4BuildingInfos.xml`
  SHA-256: `53bfcb06e4bf29e15e7ca503732b4199a5fb8ea9760216ba3f3d5e0289e83d3d`.
- `CIV4SpecialistInfos.xml`
  SHA-256: `49ff17b45392cc71687513f951b544f65d3692bb2707f40ce4598800a49f51ab`.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

### wk-settler-overflow-table

- **Tag:** `TXT_KEY_STRATEGY_WK_PEDIA`
- **Source:** `STRATEGIES_PEDIA.xml`, occurrence `0` (zero-based within that file and Tag)
- **Source SHA-256:** `b0123a4e5c5f5686ecd8c8c78f3bdc534aa98988dee16d8ed34e8d6c16cb648c`
- **Category:** `MATH_ERROR`
- **Mod version:** 1.3.3

**Fragment 1; exact occurrences: 1.**

**Original English fragment:**

```text
3rd settler 75 67
```

**Corrected English fragment:**

```text
3rd settler 75 66
```

**Fragment 2; exact occurrences: 1.**

**Original English fragment:**

```text
4th settler 100 84
```

**Corrected English fragment:**

```text
4th settler 100 83
```

Under the author’s stated model, growth takes 16 turns and later production is 6 per turn for 100-cost settlers. Carrying production overflow gives 16+ceil(300/6)=66 and 16+ceil(400/6)=83. This checks the stated model, not a new simulation of actual city growth.

**Verification:**

- `Explicit calculation`
  16 + ceil(100*n/6), n=1..4 -> 33,50,66,83
  The original example assumes 16 turns of growth and production overflow.

**Compatibility:** Historical article retained in its original version context; this is not a statement of current RoM/CoM gameplay values. See the cited primary-source versions.

## Findings left unchanged

- `TXT_KEY_EVENT_ALTERNATIVE_ENERGY_4_HELP` — FALSE_POSITIVE_AS_DESIGNED: CIVIC_ENVIRONMENTALISM is the internal Type, but its Description is TXT_KEY_CIVIC_GREEN and the English label is Green. The English civic name is correct. No English correction proposed.
- `TXT_KEY_EVENT_EARTHDAY_HELP_2` — FALSE_POSITIVE_AS_DESIGNED: CIVIC_ENVIRONMENTALISM is the internal Type, but its Description is TXT_KEY_CIVIC_GREEN and the English label is Green. The English civic name is correct. No English correction proposed.
- `TXT_KEY_EVENT_ELITE_SWORDS_HELP_1` — FALSE_POSITIVE_AS_DESIGNED: CIVIC_HEREDITARY_RULE resolves through Description=TXT_KEY_CIVIC_MONARCHY to English Monarchy in this mod. The internal identifier is not the displayed civic name. No correction proposed for that label.
- `TXT_KEY_FEAT_NATIONAL_WONDER` — DEFERRED: CoM has culture-level wonder-limit XML, but its DLL hash differs from RoM. The available AND2 rev1093 getter is not proof of CoM binary behaviour. Requires matching CoM source or targeted runtime verification.
- `TXT_KEY_HINT_28` — DEFERRED: Same CoM DLL provenance limitation as the feat text; no English patch imported from the RoM getter.
- `TXT_KEY_BUILDING_GRANGE_STRATEGY` — DEFERRED_AUTHOR_INTENT: The label is Store House while the strategy defines a grange/farm. Both could be intentionally reused content; need author intent or design evidence to choose the correct replacement. Do not invent warehouse effects.
- `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA` — VERSION_SCOPE_REVIEW_REQUIRED: The old source-defect record also flags cancellation timing, tribute refusal, land thresholds and cultural flips. Those are not silently updated from the installed Warlords 2.13 SDK because the article explicitly discusses v2.08; exact historical-version qualification is required first.
- `TXT_KEY_STRATEGY_WK_PEDIA` — SCOPED_OUT_OF_THIS_CORRECTION_SET: Other historical guide claims (religion, civic upkeep, windmill output and diplomacy) are not implicitly accepted. This file records only independently verified numerical and specialist-output corrections.
- `TXT_KEY_STRATEGY_UB_PEDIA` — NEEDS_SEPARATE_VERIFICATION: Dun upgrade interactions, Greek happiness, Forbidden Palace prerequisites, and Shale Plant power/health were not independently resolved in this pass and are not imported as corrections.
- `TXT_KEY_STRATEGY_UU_PEDIA` — DEFERRED: Industrialism enables both Panzers and SEALs. The author’s later timing assumes local oil access. Bonus Oil has TechCityTrade=Combustion, so an accurate imported-oil caveat needs trade-network code verification, not only the absence of a unit technology prerequisite.
- `TXT_KEY_STRATEGY_UU_PEDIA` — FALSE_POSITIVE_IN_PRIOR_NOTES: The article correctly speaks of ordinary macemen not selecting Drill I and of the Samurai’s intrinsic two first strikes not surviving upgrades. BtS adds free Drill I to Samurai, but that does not make the stated distinction false; keep the article wording.
- `TXT_KEY_STRATEGY_UU_PEDIA` — HISTORICAL_CAVEAT_ALREADY_PRESENT: The author already labels the Prophet skip-Masonry route pre-patch. Exact pre-patch build identity is unresolved; no current-version rewrite is inserted.
- `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA` — preserved_historical: The article intentionally preserves an early-vanilla model. No matching pre-1.61 executable/SDK was verified. Later-code differences are documented in the new version warning; replacing the historical model would falsely modernize it.
- `TXT_KEY_STRATEGY_RESEARCH_MECHS_PEDIA` — deferred: Prior review identifies the account spelling, but this mechanics audit did not independently read the named forum account. Leave the attribution for direct historical-source verification.
- `TXT_KEY_STRATEGY_SE_PEDIA` — not_confirmed_error: The English says technologies can be lightbulbed, without an explicit guarantee that one scientist always completes every technology or may freely choose one. The existing general advice is not proven false; a complete discover-action tutorial would expand the source.
- `TXT_KEY_STRATEGY_SE_PEDIA` — deferred: The prior review flags a classification problem. The Academy/building-class and Great Scientist creation records were not independently captured in this audit's primary evidence. The heading was not changed without that final check.
- `TXT_KEY_STRATEGY_SE_PEDIA` — not_confirmed_error: The English recommends copper but does not explicitly call it mandatory. XML confirms copper accelerates construction, so the advice is reasonable without changing the article.
- `TXT_KEY_STRATEGY_SE_PEDIA` — preserved_author_strategy: These are explicitly the author's strategic assumptions and invite experimentation. No universal optimum is asserted strongly enough to justify rewriting historical strategic advice as a mechanics error.
- `TXT_KEY_STRATEGY_SE_PEDIA` — preserved_context: Earlier English already explains Scientific Method removes the two free scientists. The later shorthand and Archipelago assessment are coherent with obsolescence and same-landmass specialists; no numerical modernization required.
- `TXT_KEY_STRATEGY_WAR_WEARINESS_PEDIA` — preserved_historical: The article expressly states vanilla1.61, not Warlords. Only defects within that declared ruleset were corrected.
- `TXT_KEY_STRATEGY_WAYS_HEALTHY_PEDIA` — preserved_historical: The source totals describe the enumerated historical vanilla objects. Updating to RoM/CoM would change the article's scope.
- `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA` — deferred: The text is visibly corrupted, but whether it originally meant one turn or one-to-two turns is not established. Movement depends on worker type, terrain, roads and remaining movement. Do not invent a numeric restoration without the original article or a narrowly stated replacement.
- `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA` — deferred: CvPlot::getFeatureProduction confirms working-city assignment followed by same-team nearest-city lookup. The complete CvMap::findCity tie traversal was not independently captured, so the oldest-city sentence needs a separate targeted check before correction.
- `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA` — deferred: The exact war requirement and receiving-city conditions must be checked together in CvPlot::canBuild, getFeatureProduction and worker execution. Only the production-recipient function was fully inspected in this pass; no speculative universal replacement was authored.
- `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA` — preserved_historical: The text distinguishes the editions intentionally. Retain the historical numbers and author uncertainty; do not substitute mod trait values.
- `TXT_KEY_STRATEGY_WAYS_PRODUCTION_PEDIA` — preserved_version_context: Warlords and BtS XML both grant +1 production to quarries with railroad. The article explicitly discusses those expansions; vanilla-only modernization would be wrong.

## Editorial suggestions

No optional stylistic rewrites are included. 6 suggestions are recorded outside this release.

- `TXT_KEY_STRATEGY_VASSALAGE_MECHS_PEDIA` / `vassal-weighs-decision`: The phrase may intentionally describe assigning decision weights in the AI algorithm. It is not an unambiguous language error; retain the author’s wording.
- `TXT_KEY_STRATEGY_UU_PEDIA` / `uu-qualitative-combat-claims`: Statements about units being unbeatable, guaranteed counters, likely AI behaviour or the only viable counter are strategic rhetoric or context-dependent judgments. No stylistic hedging is imported from Polish v0.2.
- `TXT_KEY_STRATEGY_UU_PEDIA` / `uu-inca-extra-settlers`: The phrase a free settler or two can include the normal initial settler rather than assert two additional settlers. Do not silently recast the intended total without author confirmation.
- `TXT_KEY_STRATEGY_UU_PEDIA` / `uu-worker-movement-comparison`: The paragraph explicitly distinguishes movement from work rate. Its no-roads and ordinary land-unit comparison is implicit. Further qualifications are editorial rather than a necessary correction.
- `TXT_KEY_STRATEGY_UU_PEDIA` / `uu-retreat-road-and-mobility-conditions`: Resource isolation, post-attack retreat, pursuit on owned roads and one-move upgrade comments rely on map/movement assumptions. The Morale exception to the last paragraph is real, but this pass leaves additional strategic qualifications for a separate optional edit rather than expanding the article.
- `TXT_KEY_STRATEGY_UU_PEDIA` / `uu-theocracy-condition-repetition`: State-religion presence is made explicit in the corrected drafting example. Repeating the condition at every later reference to Theocracy would be an editorial policy choice.

## Provenance and rights

Greywolf Forge corrections are covered by this repository’s license. Original mod text, quoted article text and earlier translations remain the work of their respective authors; this project does not relicense those underlying works.
