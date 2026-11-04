# Rehearsal commit E (disposable)

A documentation-only commit that makes release D a historical ancestor of the rehearsal `main`, so a rollback to D is a valid request. It is never deployed and is not a release:
it carries a skip instruction, has no release record, is not in the publication manifest and does not change the publication digest.
