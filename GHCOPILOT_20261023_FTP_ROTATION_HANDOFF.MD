# FTP rotation handoff: avoid duplicate credential work

**PR:** [eltonaguiar/findtorontoevents_antigravity.ca#761](https://github.com/eltonaguiar/findtorontoevents_antigravity.ca/pull/761), OPEN/unmerged.

## Completed operational work

- Verified the provided new 50webs password as user `ejaguiar1` over hostname/certificate-verified TLS.
- Verified protected-data-mode directory listing of the site, without uploading/deleting files or printing the listing.
- Updated **26 encrypted GitHub secret entries across four active deployment repositories**:
  - Primary antigravity repository:10 default/50webs/tdotevent aliases.
  - TORONTOEVENTS_ANTIGRAVITY:3 aliases.
  - STOCKSUNIFY2:3 aliases.
  - The May23 legacy copy:10 aliases; despite its name, it is not GitHub-archived and still has active deploy workflows.
- Inventory inspected FTP-secret metadata across77 owned repositories. Truly archived repos and unrelated GoDaddy/TORONTOEVENT account aliases were not blindly replaced.
- Restricted the local credential file to owner-only permissions.

No credentials appear in this note. Do not reprint local secret files, put passwords in shell command arguments, or repeat credentials in agent summaries.

## Root causes and repair

The current process inherited an obsolete `FTP_PASS`, which caused authentication failure even with the canonical local file already rotated. The new shared loader uses the local canonical value for the default50webs account, rather than that stale variable. CI without the file uses encrypted FTP-specific variables. The local file's password is never used for a different host/account; conflicting host aliases fail closed.

The PR removes the supplements deployer's hardcoded fallback; wires existing deployment entrypoints; requires verified FTPS/protected data on touched paths; stops OS-user/password fallback; separates GoDaddy credentials; and passes sports curl credentials via stdin rather than process argv.

## Peer coordination

Another agent owns broad DB/workflow credential cleanup. This PR does not edit those workflows, the shared main checkout, stashes or DB passwords. The shared audit deployer's unrelated one-line upload-list addition is not included/reverted; this PR changes only credential/TLS hunks there.

**Please do not independently re-rotate these same26 aliases or recreate the FTP loader.** Reuse/review PR761. Coordinate before touching the same deployer functions. Continue separately owned DB-secret and workflow work.

## Verification

-21 targeted tests passed, including stale-env override, CI fallback, different-account isolation, malformed inputs, protected TLS sequencing, CLI behavior and a tracked-deployer literal-default regression.
- Shell syntax and all changed Python syntax checked.
- Audit deployment dry-run passed; no content uploaded.
- Independent scoped security review found no high-confidence introduced vulnerabilities and verified the original env-only lookup directly from git.
-37,985 source/untracked files scanned for the exact current FTP password, including large files in chunks: no matches.
- All16 remote PR file bytes matched local committed bytes; final current-password/API-token scan of remote files and PR body passed.
- Hosted CI was still running at the final remote check; no claim of green full-suite CI. Existing unrelated pandas `freq="ME"` collection issue was not modified.

Safe local entrypoint:

```sh
python3 tools/ftp_credentials.py --check
python3 tools/deploy_audit_files.py --dry-run --only incidents
```

For other existing scripts, runtime environment injection is available:

```sh
python3 tools/ftp_credentials.py -- python3 tools/deploy_updates_v05.py
```

The last command deploys content if deliberately invoked; it was not executed here. The wrapper changes only the child's environment, not an already-running parent's environment.

Removing the old literal does not erase git history or previous agent transcripts. This work rotates FTP consumers, not MySQL accounts or all historical logs.
