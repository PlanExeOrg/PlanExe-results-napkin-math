# AGENTS.md

Guidance for agents (and the user) working in this repo.

## Repo layout

```
snapshot/
  <N>/                       # snapshot number, e.g. 46
    <plan_name>/             # e.g. 20250101_india_census
      meta.json              # required — points back to the zip in PlanExe-web
      ...other plan files
verify.py                    # CI check: every plan dir must have meta.json
```

## Invariant

**Every directory under `snapshot/<N>/` must contain a `meta.json`.**

CI runs `verify.py` and fails the build if any plan dir is missing it.

## What `meta.json` looks like

One entry copied verbatim from `zip_index.json` in the sibling `PlanExe-web`
repo:

```json
{
  "filename": "20250101_india_census.zip",
  "commit_id": "f6c6f66bb07f6daa1df01e83985c64b10d0e68cd",
  "commit_date": "2026-05-02T14:37:33+02:00",
  "sha256": "3658352ccfe64afd541ba5fd8fdccce66544badbe6d624d1f27b4ec73ea2e0e3"
}
```

This pins the snapshot to the exact zip artifact it was generated from.

## How to populate `meta.json` for a new plan dir

The source of truth is `zip_index.json` in the `PlanExe-web` repo. The
local clone lives at `/Users/neoneye/git/PlanExe-web/`. Use the lookup
helper (run from this repo's root):

```bash
python3 /Users/neoneye/git/PlanExe-web/lookup_zip_index.py <plan_name> > snapshot/<N>/<plan_name>/meta.json
```

The plan name may be given with or without the `.zip` suffix.

If the plan isn't in `zip_index.json` yet, the zip hasn't been published to
`PlanExe-web` — add it there first and run `python3 build_zip_index.py` to
refresh the index.

## When to do this

Whenever a new plan dir is added under `snapshot/<N>/`. Don't commit a plan
dir without its `meta.json` — CI will reject the PR.

## Verifying locally

```bash
python3 verify.py
```

Prints `OK: all <N> plan dirs have meta.json` on success, or lists the
offenders and exits non-zero.
