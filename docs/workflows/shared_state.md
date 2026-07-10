# Shared State

## Overview

The Shared State is the central data store used by the EcoVerify Agent Ecosystem. It allows all agents to exchange information without communicating directly with each other.

Every agent reads the information it needs from the Shared State and writes only the data it owns.

This approach provides:

- Loose coupling
- Better maintainability
- Easier debugging
- State persistence
- Workflow visualization
- Compatibility with LangGraph

---

# Architecture

```text
                 Coordinator
                      │
                      ▼
          ┌───────────────────────┐
          │     Shared State      │
          └───────────────────────┘
          ▲    ▲    ▲    ▲    ▲
          │    │    │    │    │
      Search Source Trust Verify Confidence
```

Instead of communicating directly:

```text
Search
   │
   ▼
Verification
```

Every agent communicates through the Shared State.

---

# Workflow

```
Coordinator
      │
      ▼
Create Shared State
      │
      ▼
Search Agent
(Read Claim)
(Write Sources)
      │
      ▼
Source Classification Agent
(Read Sources)
(Write Source Types)
      │
      ▼
Trust Agent
(Read Source Types)
(Write Trust Scores)
      │
      ▼
Verification Agent
(Read Claim + Sources + Trust Scores)
(Write Verdict)
      │
      ▼
Confidence Agent
(Read Everything)
(Write Confidence)
      │
      ▼
Coordinator
(Return Response)
```

---

# Shared State Structure

```json
{
    "claim": "",

    "sources": [],

    "source_types": [],

    "trust_scores": [],

    "verdict": "",

    "verification_reason": "",

    "confidence": 0,

    "confidence_reason": "",

    "workflow_status": "",

    "agents": {},

    "logs": []
}
```

---

# Shared State Fields

## Claim

Stores the user's verification request.

Example

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts."
}
```

---

## Sources

Stores evidence retrieved by the Search Agent.

Example

```json
{
    "sources": [
        {
            "title": "AWS Documentation",
            "url": "...",
            "content": "..."
        }
    ]
}
```

---

## Source Types

Stores classifications produced by the Source Classification Agent.

Example

```json
{
    "source_types": [
        "official",
        "research"
    ]
}
```

---

## Trust Scores

Stores trust evaluations from the Trust Agent.

Example

```json
{
    "trust_scores": [
        {
            "source": "AWS Documentation",
            "score": 10,
            "reason": "Official documentation."
        }
    ]
}
```

---

## Verdict

Stores the final verification decision.

Possible values

```
SUPPORTED
UNSUPPORTED
PARTIALLY_SUPPORTED
UNKNOWN
```

---

## Verification Reason

Explains why the verdict was chosen.

Example

```text
Multiple trusted sources support the claim.
```

---

## Confidence

Stores the confidence score.

Range

```
0 - 100
```

---

## Confidence Reason

Explains why the confidence score was assigned.

Example

```text
Three highly trusted and diverse sources consistently support the claim.
```

---

## Workflow Status

Represents the overall workflow state.

Possible values

```
Pending
Running
Completed
Failed
```

The Coordinator Agent maintains the overall workflow status.

---

## Agent Status

Each agent maintains its own execution status.

Example

```json
{
    "agents": {

        "search_agent": {
            "status": "Completed"
        },

        "source_classification_agent": {
            "status": "Completed"
        },

        "trust_agent": {
            "status": "Running"
        },

        "verification_agent": {
            "status": "Pending"
        },

        "confidence_agent": {
            "status": "Pending"
        }
    }
}
```

---

## Execution Logs

Every agent writes its own execution logs.

Example

```json
{
    "logs": [

        {
            "agent": "Search Agent",
            "message": "Generated optimized search query."
        },

        {
            "agent": "Search Agent",
            "message": "Retrieved 5 evidence sources."
        },

        {
            "agent": "Trust Agent",
            "message": "Assigned trust score 10 to AWS Documentation."
        }
    ]
}
```

---

# Read / Write Responsibilities

| Agent | Read | Write |
|---------|------|-------|
| Coordinator | Everything | Workflow Status, Final Response |
| Search Agent | Claim | Sources, Agent Status, Logs |
| Source Classification Agent | Sources | Source Types, Agent Status, Logs |
| Trust Agent | Sources, Source Types | Trust Scores, Agent Status, Logs |
| Verification Agent | Claim, Sources, Trust Scores | Verdict, Verification Reason, Agent Status, Logs |
| Confidence Agent | Claim, Sources, Trust Scores, Verdict | Confidence, Confidence Reason, Agent Status, Logs |

---

# Shared State Lifecycle

## Initial State

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts."
}
```

---

## After Search Agent

```json
{
    "claim": "...",

    "sources": [
        ...
    ]
}
```

---

## After Source Classification Agent

```json
{
    "claim": "...",

    "sources": [
        ...
    ],

    "source_types": [
        ...
    ]
}
```

---

## After Trust Agent

```json
{
    "claim": "...",

    "sources": [
        ...
    ],

    "source_types": [
        ...
    ],

    "trust_scores": [
        ...
    ]
}
```

---

## After Verification Agent

```json
{
    "claim": "...",

    "sources": [
        ...
    ],

    "source_types": [
        ...
    ],

    "trust_scores": [
        ...
    ],

    "verdict": "SUPPORTED",

    "verification_reason": "Multiple trusted sources support the claim."
}
```

---

## Final State

```json
{
    "claim": "...",

    "sources": [
        ...
    ],

    "source_types": [
        ...
    ],

    "trust_scores": [
        ...
    ],

    "verdict": "SUPPORTED",

    "verification_reason": "...",

    "confidence": 97,

    "confidence_reason": "...",

    "workflow_status": "Completed"
}
```

---

# Benefits

- Single source of truth
- Modular agent communication
- No direct agent-to-agent dependencies
- Easier debugging
- State persistence
- Execution tracking
- Workflow visualization
- Scalable architecture
- Compatible with LangGraph StateGraph
- Easy to add new agents in the future

---

# Future Extension

The Shared State is designed to support additional agents without changing the overall architecture.

Future fields may include:

- citations
- bias_analysis
- hallucination_score
- summary
- translation
- risk_assessment
- payment_status
- CAP_transaction_id
- execution_metrics

This ensures the EcoVerify Agent Ecosystem remains extensible as new capabilities are added.