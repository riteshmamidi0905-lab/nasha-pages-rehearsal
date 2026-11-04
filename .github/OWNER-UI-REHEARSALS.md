# Owner-UI rehearsal handoff — 2026-11-04

Only repository `riteshmamidi0905-lab/nasha-pages-rehearsal` is in scope. No token creation, App permission expansion, reviewer removal, bypass, production setting change or authorized-candidate edit is part of this procedure.

## Current stage: source fixture is ready; owner source action is required

Disposable main is `c7041fd549a599715988d1aa83178a4d00d6cc89`. Its exact tree is `.github/workflows/pages.yml`, `.nojekyll` and `index.html`. There are no scripts, package files, media or other non-hidden files. This fixture is not the 49-file portfolio release. Original disposable tree is preserved by restoration commit `021e9a9bfabee707d4b021076620665b283d933e`; restoration will use a normal commit, not a force push or history deletion.

Production PR #6 and production main were not modified. Current disposable Pages source remains Actions. The fixture's push workflow may pass its source guard and then fail because it intentionally has no package or build inputs. That is a fixture-staging outcome, not a portfolio regression; no build artifact, deployment or release record should result. Do not approve any fixture workflow whose artifact has not been inspected.

### Owner action 1 — select safe legacy source

1. Sign in as `riteshmamidi0905-lab` and open [disposable Settings → Pages](https://github.com/riteshmamidi0905-lab/nasha-pages-rehearsal/settings/pages).
2. Under **Build and deployment → Source**, select **Deploy from a branch**.
3. Under **Branch**, choose **main** and **/(root)**, then **Save**. Confirm main is still the fixture SHA above. Do not select another branch or any production repository.
4. Report that Save completed. The agent will inspect Pages readback, the native Pages workflow and any pending reviewer gate. If GitHub requests approval, wait for the agent to identify that exact fixture run before acting. Do not remove or bypass the gate.

Expected: build_type becomes legacy, source main at root. The native Pages build should serve only the safe fixture after its normal controls pass. The fixture index is exactly 230 bytes with SHA-256 `1119df2fc77225e73298481c1bacb1d34dcc953cea207e727fd49d64ba872926`. Until observed over HTTP, it is not considered deployed. A failed/blocked native build remains a failed/blocked scenario, not a passed transition test.

### Agent follow-up after action 1

Read source and run/job/step state; inspect fixture publication and capture every served byte/hash. While legacy is active, dispatch the existing main Pages workflow to demonstrate guard failure, downstream skips, no Pages artifact and no release record. No denied administration/review API will be retried.

If a native fixture deployment needs a reviewer, give the owner its exact run link and request **Review deployments → github-pages → Approve and deploy** for this fixture only. If the run targets a different SHA or repository, stop.

### Owner action 2 — transition back to Actions, only when prompted

After the fixture is verified live, the agent will start the read-only source-transition observer and ask the owner to change **Settings → Pages → Build and deployment → Source → GitHub Actions**. Save if a Save control is shown. Leave HTTPS, reviewers, main-only restriction and disabled bypass unchanged.

Expected: source reads workflow; observer records whether the verified fixture continues to be served. Record actual failures/interruption and sampling interval; sampled continuity does not prove no outage occurred between observations. The agent will then restore the preserved disposable tree through a normal commit and stop its resulting deploy at the reviewer gate or cancel unused runs. Do not switch the source to legacy while the restored tooling-containing tree is on main.

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
