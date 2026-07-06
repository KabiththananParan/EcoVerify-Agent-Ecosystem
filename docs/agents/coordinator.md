# Coordinator Agent

## Overview

The Coordinator Agent is the central orchestrator of the EcoVerify Agent Ecosystem. It receives verification requests, reasons about the required workflow, delegates tasks to specialized agents, maintains workflow state, aggregates results, and returns the final verification report.

Unlike other agents, the Coordinator Agent does not perform searching, trust evaluation, or verification itself. Its primary responsibility is orchestration and decision-making.

---

# Purpose

To intelligently orchestrate the verification process by:

- Understanding the incoming request
- Determining which agents are required
- Executing agents in the correct order
- Maintaining workflow state
- Collecting and aggregating results
- Returning the final verification response

---

# Agent Type

```
Intelligent Stateful Orchestrator
```

---

# Responsibilities

### 1. Receive Requests

Accept verification requests from:

- Human users
- Research agents
- RAG agents
- News agents
- Educational agents
- Financial agents
- Any external AI agent

---

### 2. Perform Workflow Reasoning

Determine:

- Which agents should be called
- Which agents can be skipped
- The optimal execution order

Example:

#### Request without sources

```json
{
  "claim": "AWS SnapStart reduces Lambda cold starts"
}
```

Workflow:

```
Search Agent
      ↓
Source Classification Agent
      ↓
Trust Agent
      ↓
Verification Agent
      ↓
Confidence Agent
```

---

#### Request with sources

```json
{
  "claim": "AWS SnapStart reduces Lambda cold starts",
  "sources": [
    "https://aws.amazon.com/..."
  ]
}
```

Workflow:

```
Source Classification Agent
      ↓
Trust Agent
      ↓
Verification Agent
      ↓
Confidence Agent
```

---

### 3. Delegate Tasks

The Coordinator Agent delegates tasks to:

- Search Agent
- Source Classification Agent
- Trust Agent
- Verification Agent
- Confidence Agent

---

### 4. Maintain Workflow State

Track:

- Current execution stage
- Agent responses
- Errors
- Completion status
- Intermediate results

---

### 5. Aggregate Results

Collect outputs from all agents and produce a final response.

---

### 6. Manage Agent Commerce

Coordinate:

- Agent-to-Agent interactions
- CAP transactions
- Payment settlement

---

# Input

## Minimal Input

```json
{
  "claim": "string"
}
```

---

## Extended Input

```json
{
  "claim": "string",
  "sources": [],
  "task": "verify"
}
```

---

# Internal Agent Calls

```text
call_search_agent()

call_source_classification_agent()

call_trust_agent()

call_verification_agent()

call_confidence_agent()
```

---

# Workflow State

Example:

```json
{
  "claim": "AWS SnapStart reduces Lambda cold starts",

  "search_completed": true,

  "sources_found": 4,

  "source_classification_completed": true,

  "trust_completed": true,

  "verification_completed": true,

  "confidence_completed": true,

  "status": "completed"
}
```

---

# Output

```json
{
  "claim": "string",

  "verdict":
    "SUPPORTED |
     UNSUPPORTED |
     PARTIALLY_SUPPORTED |
     UNKNOWN",

  "trust_score": 0,

  "confidence": 0,

  "sources": []
}
```

---

# Example Output

```json
{
  "claim":
    "AWS SnapStart reduces Lambda cold starts",

  "verdict":
    "SUPPORTED",

  "trust_score":
    95,

  "confidence":
    97,

  "sources":
  [
    "AWS Documentation",
    "AWS Blog"
  ]
}
```

---

# Called By

- Human users
- Research agents
- RAG agents
- News agents
- Educational agents
- Financial agents
- External CROO agents

---

# Does This Agent Perform AI Reasoning?

```
YES
```

Examples:

- Determine whether Search Agent is needed
- Determine whether provided sources are sufficient
- Decide workflow execution order
- Skip unnecessary agents

---

# Does This Agent Maintain State?

```
YES
```

Reasons:

- Workflow tracking
- Error recovery
- Debugging
- Visualization
- Agent orchestration

---

# Skills Learned Through This Agent

- Agent orchestration
- Multi-agent systems
- Workflow reasoning
- State management
- Agent communication
- Fault tolerance
- Dynamic execution planning
- CAP integration