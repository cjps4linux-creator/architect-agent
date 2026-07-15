# Architect Agent

Standalone architecture and design agent scaffold for the Hermes ecosystem.

Architect Agent turns a natural-language requirement into a structured system design: component boundaries, interfaces, data flow, failure modes, and a recommended technology selection. It is built to the Hermes Agent Template contract — one responsibility, explicit interfaces, bounded tool permissions, and observable behavior.

## What It Does

- Accepts a requirements brief or problem statement
- Produces a component decomposition with clear responsibilities
- Defines interfaces (inputs, outputs, contracts) between components
- Flags failure modes and recommends recovery patterns
- Selects technologies from the Hermes stack rather than inventing new ones
- Emits a design artifact that downstream Builder/Reviewer agents can consume

## Design Principles

- One primary responsibility: architecture, not implementation
- Explicit contracts over implicit assumptions
- Reuse before inventing; prefer the constrained-hardware stack
- Document failure modes as first-class output
- Observable: version, health, latency, tool usage

## Quick Start

```bash
# From the Hermes Agent Template
cp agent/AGENT.md agents/architect-agent/SOUL.md
cp agent/agent.spec.md agents/architect-agent/contract.md
python scripts/validate_agent_contract.py agents/architect-agent/contract.md
```

## Repository Layout

| Path | Purpose |
|------|---------|
| `README.md` | This file |
| `agent/` (via template) | Agent contract + soul |
| `tests/` | Contract and behavior checks |
| `LAUNCH.md` | Launch readiness snapshot |
| `SECURITY.md` | Security policy and reporting |
| `VERIFICATION.md` | Verification record |

## Integration

Architect Agent is one node in the Hermes agent graph. It is typically invoked by the Athena orchestrator after research and before implementation planning. Its output feeds the Builder and Reviewer agents.

## Status

Production-ready scaffold. The contract schema is the source of truth; the agent behavior wraps that schema.

## License

MIT — use, modify, and ship freely.
**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
