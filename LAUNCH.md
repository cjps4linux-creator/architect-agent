# Architect Agent — Launch Documentation

## Launch Readiness Snapshot

| Field | Value |
| --- | --- |
| Repo | `architect-agent` |
| Default branch | `main` |
| License | MIT |
| Commercial baseline | CI, `CONTRIBUTING.md`, `SECURITY.md`, `LAUNCH.md`, `VERIFICATION.md` |
| Purpose | Standalone architecture and design agent scaffold |

## Verified
- `README.md` present.
- No tracked `.env` files.
- `SECURITY.md` present with contact path and hardening notes.
- `.github/workflows/ci.yml` present.

## Launch Gates
- [ ] CI workflow green on `main` before release tag
- [ ] Branch protection and required status checks enabled on `main`
- [ ] GitHub secret scanning and vulnerability alerts enabled
- [ ] Agent contract schema reviewed for customer use before sale or distribution

## Release Workflow
1. Validate contract schema and README install flow against a test agent build.
2. Cherry-pick approved wording and schema updates into a release branch.
3. Tag a release with semver and attach validated example agent artifacts.
4. Rotate or revoke any shared example credentials if included in release assets.

## Support
- Support contact: `conradcjwilson0@gmail.com`
