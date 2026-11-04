# Live rehearsal results — 2026-11-04

**NO-GO pending physical Safari verification.** The owner reports a physical iPhone and Mac available; no physical test result is yet recorded.

Only the disposable repository was used. Production PR #6 remains the authorized candidate `6391698c738cab21bc60771b1035240a0c9cbd61`; no production merge or deployment was performed.

| Scenario | Run / attempt | Verified result |
|---|---|---|
| Legacy-source guard | 41889737528 | Guard failed; downstream jobs skipped; no artifacts |
| Protected native fixture | 41890208609 | Owner approval recorded; deploy succeeded; exact two-file safe fixture verified |
| Source transition | Owner UI and API | workflow publishing confirmed; pre/post fixture bytes matched; 215 matching observations across two windows, with a gap; uninterrupted availability is not claimed |
| Rejected deploy | 41884575264 / 2 | Owner rejected; deploy failed without steps; verification/recording skipped; no success record |
| Failed live verification | 41884575264 / 3 | Owner approved; deploy succeeded; incorrect verification path failed with 48 mismatches; record skipped |
| Verification-only retry | 41884575264 / 4 | Verification failed again; record skipped; same deployment ID and start time; no new approval |
| Direct record-job retry | 41884575264 / 5 | Retry accepted, but record stayed skipped because verification failed; no new deployment or success record |
| Rollback eligibility | Real evidence gate after attempt 5 | Failed run refused; no eligible release record |

## Artifact identity and preservation

Artifact 13355292866 was downloaded and independently inspected: exactly 49 approved files, 1,791,138 bytes, tree SHA-256 `fc71be319008b783e8e72a0ad6857975cc50b9eb4322d7f3d13f8a19b122b056`, no extra files, duplicates or symlinks. The current ZIP hash is `48f415e1f086a375e2870d478ffab13bc54daf91db850516d4b383711afc1258`. The earlier ZIP hash is `83bc5629c0fc284c88c8d6312185719f241915769e9da8e5ae5e6c77e7191cb8`. Both downloaded archives are preserved in [evidence/archives](evidence/archives) with checksums; the Actions upload replaced the named Pages artifact during a rerun.

The correct disposable URL independently matched 48 served files and rejected 15 tooling URLs. The zero-byte nojekyll file is part of the 49-file artifact but need not be served. This correct-URL check does not convert the intentionally failed workflow into a valid release or permit a fabricated success record.

Final disposable main is `a79385be1e3b519755823718da67bd4eaff22f4e`, restoring the exact preserved original tree. Pages uses Actions; owner review, main-only restriction and disabled bypass remain intact. All runs completed and no review is pending. Deployment ID 7555382051 was unchanged through partial retries. Earlier fixture staging/containment details and sampling limitations remain in OWNER-UI-REHEARSALS.md.

[Detailed failure/retry evidence](evidence/failed-verification-and-partial-reruns.json), verification logs, original/current archives and source-transition observations are retained in evidence/. Existing model-evaluation findings remain unchanged. Physical Safari must be completed using the adjacent test plan before a new release decision; production deployment remains separately prohibited.
