# Physical Safari verification — owner-guided record

**Status: NOT TESTED. Release decision: NO-GO pending completed physical-device evidence.** The owner reports a physical iPhone and physical Mac with Safari. No individual test is marked passed by that availability statement.

## Frozen test identity

* Production PR #6 head: `6391698c738cab21bc60771b1035240a0c9cbd61` (freshly rechecked open/unmerged).
* Test URL: https://riteshmamidi0905-lab.github.io/nasha-pages-rehearsal/
* Authorized publication: **49 files, 1,791,138 bytes**, tree SHA-256 `fc71be319008b783e8e72a0ad6857975cc50b9eb4322d7f3d13f8a19b122b056`.
* Authorized and disposable deployment manifests have the same Git blob SHA `96ba1be429c982e43db99431f827b194dbdfd333` and identical contents. The disposable deployment source is negative-test commit `f605d04b347c4f8961d500658ce7e4d9a414d039`; its publication bytes match the authorized candidate. Do not confuse its intentional workflow verification failure with different page content or a successful release record.
* Artifact `13355292866` was independently downloaded and inspected. Fresh correct-URL HTTP verification before physical testing found 48 served files byte-identical and all 15 excluded tooling URLs unavailable. The zero-byte nojekyll file accounts for the 49th artifact file and need not be served. See evidence/physical-safari-session-live-identity.txt.
* Keep the rehearsal repository and Pages settings unchanged during tests. Use the full rehearsal path, not the production root, GitHub preview renderer, an in-app browser, Responsive Design Mode or an emulator. Use the actual Safari app on each physical device.

## Recording rules

Every row starts NOT TESTED. Owner reports are recorded as user-reported; screenshots/recordings are recorded as inspected evidence only after review. A pass needs the reported outcome and the relevant evidence. Missing, ambiguous, failed and blocked checks remain explicit. Do not infer a pass from silence or from automated Chromium/WebKit tests. Do not alter model-evaluation findings.

For each batch, report: device, local date/time/timezone, test IDs, PASS/FAIL/BLOCKED/NOT TESTED, observations, and evidence references. A defect needs route, orientation/window size, exact actions, expected/actual behavior, repeatability and screenshot/recording. Do not call an intentional DENY, simulated permission refusal or copy-only tamper detection a defect.

## Batch 0 — device and browser identity

| Field | iPhone | Mac |
|---|---|---|
| Physical model | PENDING | PENDING |
| OS version/build | PENDING | PENDING |
| Safari version/build or observed identification | PENDING | PENDING |
| Page zoom, text size, content blockers, motion setting | PENDING | PENDING |
| Normal/private browsing mode | PENDING | PENDING |
| Tester/timezone/start time | PENDING | PENDING |

On iPhone: Settings → General → About; record Model Name and exact iOS version/build (tap the version entry if needed). Safari is bundled with the OS: do not guess its separate version from the iOS number. If no standalone Safari version is exposed, record that explicitly. If needed, connect the physical iPhone to the Mac, enable iPhone Safari → Advanced → Web Inspector, enable Safari developer features on Mac, and use Develop → the physical iPhone → its rehearsal tab. The read-only console expression `navigator.userAgent` records the identification actually reported by that device. Record OS/build and the observed string without inferring an exact engine binary version from it. This is inspection of the real device, not a simulator.

On Mac: Apple menu → About This Mac for model and macOS version; clicking the OS version may expose its build. Safari → About Safari gives its version/build. Typed model/version data is enough; omit serial numbers, IMEI and account details.

References: [Apple iPhone version instructions](https://support.apple.com/109065), [Mac version instructions](https://support.apple.com/109033), [Safari and OS updates](https://support.apple.com/102665).

## Batches 1–4 — physical iPhone Safari

Start in normal Safari at the rehearsal URL. Record current settings; use 100% page zoom for the baseline. Turn off orientation lock for the landscape checks. Restore temporary test settings afterward.

| ID | Check and expected result | Result | Evidence |
|---|---|---|---|
| IP01 | Home portrait: correct full URL; visible heading, fonts/images, readable text; no overlapping header, clipped content or unintended horizontal page scroll at baseline zoom | NOT TESTED | PENDING |
| IP02 | Menu opens/closes by touch; choose NASHA AI Lab; open a case study and return using browser Back; no stuck menu or lost content | NOT TESTED | PENDING |
| IP03 | Home landscape then portrait: layout remains usable, controls reachable; no blank section, overlap or clipped navigation after rotation | NOT TESTED | PENDING |
| IP04 | Open every HTML route in the coverage grid; scroll long pages; inspect portrait and landscape for clipping, table containment, missing content and visual defects | NOT TESTED | PENDING |
| IP05 | Projects search returns matches; a deliberately unmatched term shows the empty state; clear it; category filter changes results and All restores the catalog | NOT TESTED | PENDING |
| IP06 | Lab controls respond; scenario with stock 0/demand 20 reports shortfall 20; gateway DENY prevents execution; approval-required action needs separate approval before execution | NOT TESTED | PENDING |
| IP07 | Enterprise Demo: use Reset and start over if needed, complete the guided steps; switch routes/roles; read-only writes are refused; no real external action occurs | NOT TESTED | PENDING |
| IP08 | Demo governance: Verify hash chain succeeds on normal state; Run consistency check behaves correctly; Tamper test on a copy detects its intentional alteration without silently corrupting the active state | NOT TESTED | PENDING |
| IP09 | Data Lab query selection updates the visible query/result/chart; tables remain usable by touch; demo-state integration displays the expected synthetic state | NOT TESTED | PENDING |
| IP10 | Reload home/explorer/case pages several times: no persistent blank/transparent content. Demo state persists on reload where designed; browser Back/Forward stays usable | NOT TESTED | PENDING |
| IP11 | Local links and resume PDF open correctly; intentional external links reach their destinations. Do not send email or submit any external message | NOT TESTED | PENDING |
| IP12 | Zoom/enlarged text remains readable and controls reachable. At zoomed magnification panning can be normal; distinguish it from baseline page overflow. Reduce Motion leaves content visible and controls functional | NOT TESTED | PENDING |
| IP13 | VoiceOver smoke: meaningful heading/link/button names, logical reading/focus order, operable menu and form labels, understandable result/status announcements; no focus trap | NOT TESTED | PENDING |
| IP14 | Missing URL displays the designed not-found page with usable recovery link; supported portfolio fallback stays readable when JavaScript is temporarily disabled; demos explain their JS dependency; restore JavaScript before continuing | NOT TESTED | PENDING |

**Batch 1 only:** IP01–IP03. Open home portrait; capture it; open/close the menu, navigate to lab/case and Back; rotate home to landscape and back. Report those three results and evidence before moving on.

**Batch 2:** IP04–IP06, page coverage and project/lab interactions. **Batch 3:** IP07–IP10, demo/Data Lab/reload. **Batch 4:** IP11–IP14, links/accessibility/fallback. We will guide exact controls as each batch begins.

For VoiceOver, establish a reliable off shortcut first (Accessibility Shortcut can toggle VoiceOver with a triple click of the side/Home button), then use Settings → Accessibility → VoiceOver. Swipe to move focus, double-tap to activate. Record actual spoken labels and results; if unable to test, record BLOCKED rather than PASS. Reduced Motion is under Accessibility → Motion. If available on the installed version, JavaScript is in Settings → Apps → Safari → Advanced (older versions put Safari directly in Settings). Record and restore the original value.

## Batches 5–7 — physical macOS Safari

Use a real Safari window, first wide and then narrowed normally. Do not use device emulation as an iPhone result. Record window dimensions if known, page zoom and keyboard-navigation settings.

| ID | Check and expected result | Result | Evidence |
|---|---|---|---|
| MS01 | Home and all coverage routes load and scroll correctly at normal width: fonts/images/long content present, no visual defects or unexpected requests/errors observed | NOT TESTED | PENDING |
| MS02 | Narrow the actual window and widen it again: navigation, text, cards and tables reflow without overlap or lost controls; menu opens/closes where applicable | NOT TESTED | PENDING |
| MS03 | Keyboard: visible focus, skip link reaches main content, logical Tab/Shift-Tab order; menu works by keyboard and Escape closes it with focus returned appropriately | NOT TESTED | PENDING |
| MS04 | Project search/filter/empty state and lab architecture/scenario/gateway controls behave correctly using keyboard and mouse | NOT TESTED | PENDING |
| MS05 | Complete demo guide; inspect every demo route; role restrictions, audit verification, copy-only tamper test and consistency check behave as described | NOT TESTED | PENDING |
| MS06 | Data Lab query/results/charts and table scrolling work; synthetic demo-state integration remains consistent | NOT TESTED | PENDING |
| MS07 | Repeated reload, Back/Forward, designed persistence/reset, PDF/local/external links and missing-page recovery behave correctly | NOT TESTED | PENDING |
| MS08 | Browser zoom to 200% and normal-window reflow: text readable, controls reachable, no content loss; test Reduce Motion and restore preferences | NOT TESTED | PENDING |
| MS09 | VoiceOver smoke: correct semantics, useful names, logical order, form labels and announced dynamic results; no keyboard/screen-reader trap | NOT TESTED | PENDING |
| MS10 | Supported no-JavaScript fallback and clear demo dependency; restore JavaScript. Inspect Safari Web Inspector console/network during interactions; record actual errors or explicitly unavailable observations | NOT TESTED | PENDING |

**Batch 5:** MS01–MS03. **Batch 6:** MS04–MS07. **Batch 7:** MS08–MS10. Record Safari's link-focus preference (Advanced → Press Tab to highlight each item on a webpage, if present). A platform preference must be distinguished from an app focus defect; record any temporary change. VoiceOver can normally be toggled with Command-F5 (or the applicable hardware shortcut); set up a reliable off method first. Safari developer features expose Web Inspector and JavaScript controls; do not run arbitrary console commands or clear browser-wide data.

## Route coverage — complete on both devices

Each route needs a reported outcome; use a recording/timestamp or screenshot reference where relevant. The grid starts NOT TESTED on both devices.

| Route under the rehearsal base | iPhone portrait / landscape | Mac wide / narrow | Evidence or defect |
|---|---|---|---|
| 404.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| ai-engineering.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-genai-doc-assistant.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-llm-eval-framework.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-mcp-weir.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-nasha-ai-lab-architecture.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-production-ai-agent-platform.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-studies.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| case-support-escalation-copilot.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| data-lab.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| demo/index.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| index.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| lab-explorer.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| nasha-lab.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| projects.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| recruiter.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |
| verified-projects.html | NOT TESTED / NOT TESTED | NOT TESTED / NOT TESTED | PENDING |

Also visit the demo views: dashboard, guide, technical, sales, inventory, finance, departments, departments/finance, hr, marketing, support, bi, agents, governance and infra. Record blank views, clipping or unusable tables explicitly. Test a deliberate missing path such as `safari-missing-page-check`; the expected not-found page is not a broken-page defect.

## Evidence captures

Use real device captures. Keep Safari UI and the rehearsal URL visible when practical so the tested site is identifiable. A typed device/version record is enough; do not include serial/account screens.

* iPhone: home portrait, home landscape, open menu/narrow navigation, and demonstrated demo/Data Lab results. A short screen recording of menu → lab/case → Back → rotation is useful. Capture every defect at the failing orientation and add reproduction steps.
* Mac: About Safari version/build, wide home, narrowed navigation or table, visible keyboard focus/skip-link result, and demo/Data Lab result. A short recording can show keyboard navigation/Escape. Capture any defect separately.
* Standard screenshot shortcuts: Face ID iPhone side + volume-up (Home-button devices use the applicable Home + side/top combination); Mac Shift-Command-4 for a selection/window. Screen recording is available in iPhone Control Center and Mac Shift-Command-5. Recordings supplement, rather than replace, per-check reported results.
* Evidence labels: IP01-home-portrait, IP03-home-landscape, IP02-menu-navigation, IP07-demo, IP09-data-lab; MS-version, MS01-home-wide, MS02-narrow, MS03-keyboard, MS05-demo. Add device/time or a simple sequence number.

We will inspect supplied evidence and keep user-reported versus directly observed results distinct. Missing evidence, open defects and untested checks stay visible. No production merge is permitted until mandatory results are accepted and the unchanged head, safeguards, required checks and artifact identity are freshly reverified. Production deployment remains separately prohibited.

## Results ledger

No physical test result has been supplied yet. Device metadata and each batch remain pending. The owner has reported physical iPhone/Mac availability only. No simulated result is counted.
