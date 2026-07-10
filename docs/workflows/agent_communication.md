# Agent Communication

## Overview

The EcoVerify Agent Ecosystem follows a centralized communication architecture where the **Coordinator Agent** is responsible for all communication between agents.

Specialized agents never communicate directly with each other. Instead, they exchange information through the **Coordinator Agent** and the **Shared State**.

This design keeps the system modular, maintainable, and scalable.

---

# Communication Architecture

```text
                     Human / AI Agent
                            │
                            ▼
                  Coordinator Agent
                            │
        ┌──────────┬────────┼────────┬────────┐
        ▼          ▼        ▼        ▼        ▼
   Search     Source      Trust   Verification Confidence
    Agent   Classification Agent      Agent       Agent
        ▲          ▲        ▲        ▲        ▲
        └──────────┴────────┴────────┴────────┘
                     Shared State
```

---

# Communication Principles

The EcoVerify Agent Ecosystem follows these principles:

- Coordinator controls the workflow.
- Agents never communicate directly.
- Every agent reads from the Shared State.
- Every agent writes only the data it owns.
- Every agent reports its execution status.
- Every agent writes execution logs.

---

# Communication Lifecycle

Every agent follows the same execution lifecycle.

```text
Receive Task
      │
      ▼
Read Shared State
      │
      ▼
Perform Task
      │
      ▼
Write Results
      │
      ▼
Write Execution Log
      │
      ▼
Update Agent Status
      │
      ▼
Return Control to Coordinator
```

This lifecycle is identical for every agent in the ecosystem.

---

# Communication Flow

## Step 1

Coordinator receives a request.

Example

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts."
}
```

---

## Step 2

Coordinator determines which agent should execute first.

Example

```
Search Agent
```

---

## Step 3

Coordinator sends a task.

Example

```json
{
    "task": "search",
    "claim": "AWS SnapStart reduces Lambda cold starts."
}
```

---

## Step 4

Search Agent

- Reads the claim
- Searches for evidence
- Writes sources to Shared State
- Updates status
- Returns control

---

## Step 5

Coordinator reads the updated Shared State.

It determines the next agent.

---

## Step 6

Coordinator sends the next task.

Example

```json
{
    "task": "classify_sources"
}
```

---

## Step 7

The process continues until every required agent completes.

---

# Standard Communication Contract

Every agent follows the same communication contract.

## Input

```json
{
    "task": "...",
    "shared_state": {}
}
```

---

## Process

```
Read Shared State

↓

Execute Task

↓

Update Shared State

↓

Log Execution

↓

Update Status

↓

Return
```

---

## Output

```json
{
    "status": "completed"
}
```

Possible status values

```
Pending

Running

Completed

Failed
```

---

# Task Messages

## Search Agent

```json
{
    "task": "search",
    "claim": "..."
}
```

---

## Source Classification Agent

```json
{
    "task": "classify_sources"
}
```

---

## Trust Agent

```json
{
    "task": "evaluate_trust"
}
```

---

## Verification Agent

```json
{
    "task": "verify_claim"
}
```

---

## Confidence Agent

```json
{
    "task": "calculate_confidence"
}
```

---

# Shared State Communication

Agents communicate indirectly through the Shared State.

Example

```
Coordinator

↓

Shared State

↓

Search Agent

writes

sources

↓

Shared State

↓

Source Classification Agent

reads

sources

writes

source_types

↓

Shared State

↓

Trust Agent

reads

source_types

writes

trust_scores
```

This continues until the workflow completes.

---

# Agent Status Updates

Each agent updates only its own status.

Example

```json
{
    "search_agent": {
        "status": "Completed"
    }
}
```

Another example

```json
{
    "trust_agent": {
        "status": "Running"
    }
}
```

The Coordinator monitors the status of all agents to determine the overall workflow state.

---

# Execution Logs

Each agent records its own execution logs.

Example

```json
{
    "agent": "Search Agent",
    "message": "Generated optimized search query."
}
```

```json
{
    "agent": "Search Agent",
    "message": "Retrieved 5 evidence sources."
}
```

```json
{
    "agent": "Trust Agent",
    "message": "Assigned trust score 10 to AWS Documentation."
}
```

Logs are stored in the Shared State.

---

# Error Communication

If an agent encounters an error, it reports the failure to the Coordinator.

Example

```json
{
    "status": "Failed",
    "reason": "Search service unavailable."
}
```

The Coordinator decides how to proceed.

Possible actions:

- Retry the task
- Skip the task
- Stop the workflow
- Return an error response

---

# Dynamic Communication

The Coordinator dynamically selects the required agents based on the request.

Example

```
Verify Claim

↓

Search

↓

Classification

↓

Trust

↓

Verification

↓

Confidence
```

---

Another example

```
Trust Evaluation

↓

Classification

↓

Trust
```

---

Another example

```
Evidence Search

↓

Search
```

Only the required agents are executed.

---

# Benefits

This communication architecture provides:

- Centralized orchestration
- Loose coupling
- Modular design
- Easier debugging
- Dynamic workflow execution
- Better scalability
- Easier maintenance
- Reusable agents
- Simplified error handling
- Compatibility with LangGraph
- Compatibility with CROO Agent Protocol (CAP)

---

# Future Enhancements

The communication architecture is designed to support new agents without changing existing communication patterns.

Future agents may include:

- Citation Agent
- Explainability Agent
- Bias Detection Agent
- Hallucination Detection Agent
- Translation Agent
- Risk Assessment Agent
- Summarization Agent

Since every agent follows the same communication contract, new agents can be integrated seamlessly into the ecosystem.