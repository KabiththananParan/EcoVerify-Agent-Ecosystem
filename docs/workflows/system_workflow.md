# System Workflow

## Overview

The EcoVerify Agent Ecosystem follows an orchestrator-based architecture where the **Coordinator Agent** manages the entire verification workflow. Rather than every agent communicating with each other, all communication flows through the Coordinator Agent.

This architecture keeps the system modular, maintainable, and easy to extend.

---

# Architecture

```text
                    Human / AI Agent
                           │
                           ▼
                 Coordinator Agent
                           │
                           ▼
                   Search Agent
                           │
                           ▼
          Source Classification Agent
                           │
                           ▼
                    Trust Agent
                           │
                           ▼
                 Verification Agent
                           │
                           ▼
                  Confidence Agent
                           │
                           ▼
                 Coordinator Agent
                           │
                           ▼
                    Final Response
```

---

# Why an Orchestrator?

The Coordinator Agent acts as the central controller of the ecosystem.

Responsibilities:

- Receive requests
- Understand user intent
- Decide which agents should be executed
- Skip unnecessary agents
- Maintain workflow state
- Aggregate results
- Return the final response

Each specialized agent performs only one responsibility.

---

# Main Verification Workflow

## Step 1 — Receive Request

Input

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts."
}
```

↓

Coordinator Agent receives the request.

---

## Step 2 — Analyze Request

The Coordinator determines:

- Is this a verification request?
- Are sources already provided?
- Which agents are required?

---

## Step 3 — Search Evidence

If no sources are provided, the Coordinator calls the Search Agent.

The Search Agent:

- Generates optimized search queries
- Searches multiple sources
- Collects relevant evidence
- Returns structured search results

---

## Step 4 — Classify Sources

The Coordinator sends the retrieved sources to the Source Classification Agent.

The Source Classification Agent classifies each source as:

- Official
- Research
- Government
- News
- Technical
- Organization
- Community
- Personal

---

## Step 5 — Evaluate Trust

The Coordinator sends classified sources to the Trust Agent.

The Trust Agent evaluates each source and assigns:

- Trust Score (1–10)
- Explanation

Example:

| Source | Type | Trust |
|--------|------|------:|
| AWS Documentation | Official | 10 |
| Nature | Research | 10 |
| Reuters | News | 8 |
| Medium Blog | Personal | 3 |

---

## Step 6 — Verify Claim

The Coordinator sends:

- Claim
- Evidence
- Trust Scores

to the Verification Agent.

The Verification Agent determines:

- SUPPORTED
- UNSUPPORTED
- PARTIALLY_SUPPORTED
- UNKNOWN

---

## Step 7 — Calculate Confidence

The Coordinator sends the verification result to the Confidence Agent.

The Confidence Agent considers:

- Trust scores
- Evidence count
- Source agreement
- Contradictions
- Source diversity

It returns:

- Confidence Score (0–100)
- Explanation

---

## Step 8 — Return Response

The Coordinator aggregates all results into a single response.

Example:

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts.",
    "verdict": "SUPPORTED",
    "confidence": 97,
    "sources": [
        "AWS Documentation",
        "AWS Blog",
        "Research Paper"
    ]
}
```

The response is returned to the client.

---

# Dynamic Workflows

The Coordinator intelligently selects the workflow based on the request.

---

## Workflow A — Verify a Claim

### Input

```json
{
    "claim": "..."
}
```

Workflow

```text
Coordinator
      │
      ▼
Search
      │
      ▼
Source Classification
      │
      ▼
Trust
      │
      ▼
Verification
      │
      ▼
Confidence
      │
      ▼
Response
```

---

## Workflow B — Verify a Claim with User Sources

### Input

```json
{
    "claim": "...",
    "sources": [...]
}
```

Workflow

```text
Coordinator
      │
      ▼
Source Classification
      │
      ▼
Trust
      │
      ▼
Verification
      │
      ▼
Confidence
      │
      ▼
Response
```

Search Agent is skipped because evidence is already provided.

---

## Workflow C — Check Source Trustworthiness

### Input

```json
{
    "source": "https://example.com"
}
```

Workflow

```text
Coordinator
      │
      ▼
Source Classification
      │
      ▼
Trust
      │
      ▼
Response
```

Verification is not required.

---

## Workflow D — Find Evidence Only

### Input

```json
{
    "claim": "...",
    "task": "search"
}
```

Workflow

```text
Coordinator
      │
      ▼
Search
      │
      ▼
Response
```

Only evidence retrieval is performed.

---

# Agent Communication

Agents never communicate directly.

All communication flows through the Coordinator.

```text
        Coordinator
        /   |   \
       /    |    \
 Search  Trust  Verify
       \    |    /
        \   |   /
     Confidence
```

This provides:

- Loose coupling
- Easier maintenance
- Better debugging
- Flexible workflows

---

# Workflow Summary

| Step | Agent | Responsibility |
|------|-------|----------------|
| 1 | Coordinator | Receive and analyze request |
| 2 | Search | Retrieve evidence |
| 3 | Source Classification | Categorize sources |
| 4 | Trust | Evaluate source credibility |
| 5 | Verification | Determine claim validity |
| 6 | Confidence | Estimate certainty |
| 7 | Coordinator | Aggregate and return response |

---

# Benefits of This Architecture

- Modular agent design
- Single responsibility per agent
- Dynamic workflow execution
- Easy debugging through centralized orchestration
- Reusable agents
- Scalable architecture
- Suitable for Agent-to-Agent (A2A) communication
- Compatible with CROO CAP integration

---

# Future Enhancements

The architecture is designed to support additional agents without modifying existing workflows.

Possible future agents include:

- Citation Agent
- Summarization Agent
- Bias Detection Agent
- Hallucination Detection Agent
- Explainability Agent
- Translation Agent
- Risk Assessment Agent

The Coordinator can incorporate new agents into the workflow as needed while preserving the overall architecture.