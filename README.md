# Architect Agent

Standalone architecture and design agent scaffold for the Hermes ecosystem.

Architect Agent turns a natural-language requirement into a structured system design: component boundaries, interfaces, data flow, failure modes, and a recommended technology selection. It is built to the Hermes Agent Template contract  -  one responsibility, explicit interfaces, bounded tool permissions, and observable behavior.

Built by Conrad CJ Wilson.

## What It Does

| Capability | Implementation |
|---|---|
| Requirements decomposition | Accepts a natural-language brief and produces component boundaries |
| Interface definition | Explicit inputs, outputs, and contracts between components |
| Data flow mapping | Visual and textual representation of how data moves through the system |
| Failure mode analysis | Identifies single points of failure and recommends recovery patterns |
| Technology selection | Chooses from the Hermes stack rather than inventing new dependencies |
| Design artifact output | Produces a structured artifact that downstream Builder and Reviewer agents can consume |

## Repository Layout

| Path | Purpose |
|---|---|
| `agent/AGENT.md` | Agent identity and execution profile |
| `agent/agent.spec.md` | Formal contract schema |
| `tests/` | Contract and behavior checks |
| `LAUNCH.md` | Launch readiness snapshot |
| `SECURITY.md` | Security policy and reporting |
| `VERIFICATION.md` | Verification record |

## Design Principles

- One primary responsibility: architecture, not implementation
- Explicit contracts over implicit assumptions
- Reuse before inventing; prefer the constrained-hardware stack
- Document failure modes as first-class output
- Observable: version, health, latency, tool usage

## Integration

Architect Agent is one node in the Hermes agent graph. It is typically invoked by the Athena orchestrator after research and before implementation planning. Its output feeds the Builder and Reviewer agents.

## Quick Start

```bash
# From the Hermes Agent Template
cp agent/AGENT.md agents/architect-agent/SOUL.md
cp agent/agent.spec.md agents/architect-agent/contract.md
python scripts/validate_agent_contract.py agents/architect-agent/contract.md
```

## License

MIT  -  use, modify, and ship freely.

**Author:** Conrad CJ Wilson
**GitHub:** https://github.com/cjps4linux-creator
**LinkedIn:** https://www.linkedin.com/in/conradcjwilson
