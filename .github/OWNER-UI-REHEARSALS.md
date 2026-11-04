# Owner-UI rehearsal handoff — 2026-11-04

Only repository `riteshmamidi0905-lab/nasha-pages-rehearsal` is in scope. No token creation, App permission expansion, reviewer removal, bypass, production setting change or authorized-candidate edit is part of this procedure.

## Current stage: rejection verified; owner approval for failed-verification rehearsal pending

Latest rejection checkpoint: run `41884575264`, attempt 2, completed failure after review history recorded owner `riteshmamidi0905-lab` rejecting environment `26178437285`. Deploy failed without executing steps; verify-live and record-release were skipped. The only artifact is the existing verified github-pages artifact; no release-record artifact exists. The real rollback evidence gate independently refused the commit because this run did not complete successfully. [Evidence](evidence/rejected-deployment-attempt-2.json).

The next owner action is a current deploy-job retry (attempt 2 job `126795759741`), followed by approval of the fresh disposable-only gate. Its intentionally incorrect live-verification path must then fail and produce no successful release record. The original artifact remains unexpired with its verified archive digest; owner reviewer, main-only policy and disabled bypass remain intact. NO-GO still applies pending this actual failure path, partial reruns and physical Safari.

Latest checkpoint: the API now independently confirms build_type workflow, and the live fixture still matches its expected bytes. Guarded restoration commit `a79385be1e3b519755823718da67bd4eaff22f4e` restores the exact original disposable tree. Unused restoration runs were cancelled before deployment. The functional source-transition rehearsal is complete, with 215 matching HTTP observations across two windows and matching pre/post bytes. There is a gap between windows and the precise settings-write time is not known; uninterrupted availability is not claimed. Raw observations and hashes are retained in [evidence/source-transition-checkpoint.json](evidence/source-transition-checkpoint.json). The next owner step is deploy-only retry and Reject on negative run 41884575264; no further source-setting change is requested.

Historical staging observations follow; the checkpoint above supersedes their earlier blocked/awaiting states.

Owner confirmed legacy publishing from main at root. Native [run 41890208609](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/actions/runs/41890208609) completed successfully. Its downloaded artifact `13351694876` contains only the verified 230-byte index.html and empty .nojekyll. Review history explicitly records approval by riteshmamidi0905-lab for environment 26178437285; admin bypass remains disabled. Deployment 7554724604 has latest status success. The owner reported the UI banner “There was a problem approving one of the gates.” Its cause is unknown, but the independent server records establish that the fixture approval/deployment succeeded. Both root and index.html match the fixture hash; package.json, scripts/ and the hidden workflow URL return 404.

The return-to-Actions UI action was reported saved, but subsequent fresh and cache-busted API reads still reported legacy. The full source-transition test is NOT PASSED. Keep the minimal fixture on main until Actions mode is independently confirmed; do not infer source state from a UI success message alone.

Disposable main is `9f892bf91fb99823f4a4f143ca59e4bf78d6efa3`; its safe fixture tree equals `d70aba3cfcf8bf19c7168263d4bc876a3b893220` and `c7041fd549a599715988d1aa83178a4d00d6cc89`. Its exact tree is `.github/workflows/pages.yml`, `.nojekyll` and `index.html`. There are no scripts, package files, media or other non-hidden files. This fixture is not the 49-file portfolio release. Original disposable tree is preserved by restoration commit `021e9a9bfabee707d4b021076620665b283d933e`; restoration will use a normal commit, not a force push or history deletion.

Production PR #6 and production main were not modified. Current disposable Pages source remains Actions. The fixture's push workflow may pass its source guard and then fail because it intentionally has no package or build inputs. That is a fixture-staging outcome, not a portfolio regression; no build artifact, deployment or release record should result. Do not approve any fixture workflow whose artifact has not been inspected.

Observed staging result: [run 41889140649](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/actions/runs/41889140649) completed with guard success, setup-node failure in build (fixture has no package lock), and deploy/verify-live/record-release skipped. Artifact inventory is empty and no reviewer approval is pending. This is not the legacy guard test; that test starts only after owner action 1 changes the source.

### Owner action 1 — select safe legacy source

1. Sign in as `riteshmamidi0905-lab` and open [disposable Settings → Pages](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/settings/pages).
2. Under **Build and deployment → Source**, select **Deploy from a branch**.
3. Under **Branch**, choose **main** and **/(root)**, then **Save**. Confirm main is still the fixture SHA above. Do not select another branch or any production repository.
4. Report that Save completed. The agent will inspect Pages readback, the native Pages workflow and any pending reviewer gate. If GitHub requests approval, wait for the agent to identify that exact fixture run before acting. Do not remove or bypass the gate.

Expected: build_type becomes legacy, source main at root. The native Pages build should serve only the safe fixture after its normal controls pass. The fixture index is exactly 230 bytes with SHA-256 `1119df2fc77225e73298481c1bacb1d34dcc953cea207e727fd49d64ba872926`. Until observed over HTTP, it is not considered deployed. A failed/blocked native build remains a failed/blocked scenario, not a passed transition test.

Owner action 1 is confirmed: Pages is legacy from main at root. [Run 41889737528](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/actions/runs/41889737528) completed with guard failure at the source check, downstream build/deploy/verify-live/record-release skipped, and an empty artifact inventory. The guard log records exit code 1. This is a passed live legacy-source refusal test; it does not establish transition continuity. The URL still served the prior portfolio when checked, and latest native Pages build returned 404. A content-preserving fixture commit was pushed to trigger branch publication; its actual native build/deployment must still be observed before owner action 2.

### Agent follow-up after action 1

Read source and run/job/step state; inspect fixture publication and capture every served byte/hash. While legacy is active, dispatch the existing main Pages workflow to demonstrate guard failure, downstream skips, no Pages artifact and no release record. No denied administration/review API will be retried.

If a native fixture deployment needs a reviewer, give the owner its exact run link and request **Review deployments → github-pages → Approve and deploy** for this fixture only. If the run targets a different SHA or repository, stop.

### Owner action 2 — transition back to Actions, only when prompted

After the fixture is verified live, the agent will start the read-only source-transition observer and ask the owner to change **Settings → Pages → Build and deployment → Source → GitHub Actions**. Save if a Save control is shown. Leave HTTPS, reviewers, main-only restriction and disabled bypass unchanged.

Expected: source reads workflow; observer records whether the verified fixture continues to be served. Record actual failures/interruption and sampling interval; sampled continuity does not prove no outage occurred between observations. The agent will then restore the preserved disposable tree through a normal commit and stop its resulting deploy at the reviewer gate or cancel unused runs. Do not switch the source to legacy while the restored tooling-containing tree is on main.

## Premature restoration incident and containment

After an API assertion reported legacy, a shell sequence incorrectly continued and pushed restoration commit `c36844d1bdd53317fb43b5e63815ddd3756aea53`. This was an execution error: restoration must have been conditional on confirmed Actions source. Safe-fixture commit `9f892bf91fb99823f4a4f143ca59e4bf78d6efa3` immediately restored the exact three-file safe tree through a normal fast-forward push. No production repository was modified.

Native run `41891227555` for the premature restoration was cancelled before deployment: build/report jobs succeeded, deploy was cancelled with no steps, review history is empty and no approval remains pending. The custom Pages run failed its legacy guard. Follow-up safe-fixture native run `41891291234` was cancelled to avoid an unnecessary extra deployment. The live fixture still matched its original 230-byte hash. These observations establish containment; the cancelled native run is not a successful release or a rejected-review rehearsal.

Future restoration must use a single guarded control path: abort the entire operation unless fresh Pages readback is workflow, require main's expected SHA, and recheck the source immediately before the push. A failed assertion must not be followed by unconditional shell commands. No restoration is currently authorized while readback is legacy.

## Next stage: rejected deployment, then failed live verification

Do not do this stage while source is legacy or main is the fixture. Wait for the agent to confirm restoration and Actions publishing.

The existing negative test is [run 41884575264](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/actions/runs/41884575264), pinned to `f605d04b347c4f8961d500658ce7e4d9a414d039`. Its guard/build succeeded and its artifact was independently verified against the authorized 49-file manifest and digest. The workflow intentionally checks a nonexistent live-verification path. Its previous attempt was cancelled before deployment.

1. Owner opens the run in the disposable repository. Use the current deploy job's rerun control if GitHub exposes it; otherwise **Re-run jobs → Re-run failed jobs**, if offered. If the only option is **Re-run all jobs**, report that before starting so the agent can distinguish the necessary fresh build from reused evidence. Old recorded deploy job ID `126766932319` belongs to attempt 1; recheck the latest attempt before using any ID.
2. Wait for the fresh deploy reviewer gate. Confirm repository, run SHA, artifact identity and environment. Choose **Review deployments → github-pages → Reject**, with a comment identifying the rejection rehearsal. Report completion.
3. Agent collects the attempt's jobs/steps/artifacts and verifies deploy failed, later verification/recording did not succeed, and no successful release record exists.
4. After evidence capture, owner stages another deploy retry using the UI. Agent verifies a fresh required-review gate. Owner selects **Review deployments → github-pages → Approve and deploy** for this disposable negative run only.
5. Expected: deploy succeeds, verify-live fails against the intentionally wrong path, record-release is skipped or fails, and no successful release record exists. A pending, rejected or cancelled deploy does not prove this scenario ran.

Automatic approval review rejected the agent's attempt to stage the cancelled deploy retry, citing the unchanged missing Deployments permission. No workaround was used. Owner UI staging is required; the agent can still inspect results using current read access. This rejection is separate from GitHub reviewer decisions and is not a failed-deployment test result.

## Partial reruns after actual failed verification

After the failure above is observed, the agent can exercise available current-attempt verification-job and record-job reruns using Actions permissions. If a staging action is refused, the owner can use the corresponding job UI after the agent identifies the exact current job. Record which dependencies actually rerun. A deploy rerun requires a new owner review. A verifier-only rerun that does not deploy is not an approval bypass.

The verifier must still fail for the intentional fault; the record writer must not create a successful record from failure/skipped/cancelled verification. Inspect run attempts, job/step results, artifact inventory and rollback evidence-gate refusal. GitHub API refusals are recorded as refusals, not successful test executions. Do not retry stale-attempt job IDs or bypass any gate.

## Physical Safari checklist and required evidence

Physical Safari remains a mandatory blocker. Use physical Apple hardware or an authenticated service session explicitly designated a real iOS device. No physical-device session is currently accessible to the agent. WebKit, simulators and unverified cloud desktop hardware do not establish physical-device coverage.

Test the verified 49-file candidate artifact, not the source-transition fixture or the older production baseline. Expected publication is 1,791,138 bytes and tree digest `fc71be319008b783e8e72a0ad6857975cc50b9eb4322d7f3d13f8a19b122b056`; candidate head is `6391698c738cab21bc60771b1035240a0c9cbd61`. Use a local HTTP server with an authenticated testing tunnel, or an existing disposable deployment whose bytes the agent has verified. Do not publish an alternate production site.

* Open every published HTML page. Check fonts/images/links, portrait/landscape, narrow/desktop layouts, no page overflow, clipping or overlapping headers.
* Test menu open/close, navigation and back/forward, project search/filter/empty state; on Mac check keyboard focus, skip link and Escape behavior.
* Exercise lab controls and approval/execution separation including denied actions; run the synthetic Enterprise Demo guide/role restrictions/audit check and Data Lab query interactions.
* Check initial/repeat load, reload/scroll, reduced motion, storage/reset and supported no-JavaScript fallback. Record observable Safari console/network errors; do not claim unobserved checks passed.
* Capture screenshots/video and pass/fail/reproduction details for each tested device and interaction. Use the adjacent evidence template.

## Completion gate

Collect actual run IDs, attempt IDs, logs, job/step outcomes, artifacts, reviewer decisions, source readbacks and restoration evidence before updating the release decision. Preserve logs and release records; delete none. All mandatory rehearsals and physical Safari evidence must pass before a fresh authorized-head/protection check can permit squash merge. No production deployment approval is authorized.

## Source selector persistence diagnostic

GitHub's [documented Actions source procedure](https://docs.github.com/en/pages/getting-started-with-github-pages/configuring-a-publishing-source-for-your-github-pages-site) requires selecting Source → GitHub Actions; it has no separate Save step. The branch-publishing procedure has the Save button. Its absence/disabled state is not, by itself, a failure. However, the fresh cache-busted readback at 2026-11-04 18:55:09 UTC still reported build_type legacy, source main/root, main at the safe fixture SHA. At that earlier readback the source transition remained blocked; the later independently confirmed workflow checkpoint above supersedes that state. The status errored corresponds to the cancelled latest native build; it does not establish that the live fixture is unavailable.

Exact next owner diagnostic: open the disposable settings URL directly in a full browser tab signed in as the owner. Open Developer Tools → Network, clear the log, select GitHub Actions once, wait for the setting request to finish, then reload. Report the Source value after reload plus the setting-update request's HTTP status and any displayed error text. Do not send authorization headers, cookies, tokens or an unredacted HAR. If selection produces no request, report that fact and any visible client-side error. The agent must independently observe build_type workflow before restoring the original tree. Do not configure a starter workflow, create a token, expand App grants or approve another deployment to diagnose this.

The adjacent restore-disposable.py uses a single Python control path: read-only by default, exact disposable repository and expected main SHA, fresh workflow-source checks before every mutation phase, check=True subprocesses, and a normal force=false ref update. It must stop under the current legacy mode. The owner must leave source settings unchanged while a future confirmed restoration executes. This helper was not used to restore or modify main in this blocked state.
