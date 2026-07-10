# LangGraph Workflow

## Overview

EcoVerify uses **LangGraph** to orchestrate the execution of multiple AI agents. Instead of writing sequential function calls, LangGraph represents the entire verification process as a workflow graph where each specialized agent is a node and the Shared State flows between them.

This architecture enables:

- Dynamic workflow execution
- Conditional routing
- Shared state management
- Modular agent design
- Easy scalability

---

# Why LangGraph?

LangGraph is well suited for EcoVerify because it provides:

- Stateful workflows
- Multi-agent orchestration
- Conditional execution
- Shared memory
- Easy debugging
- Flexible workflow routing

Each EcoVerify agent becomes a **LangGraph Node**, while the **Shared State** becomes the graph state.

---

# LangGraph Architecture

```text
                    START
                      │
                      ▼
              Coordinator Agent
                      │
        ┌─────────────┴─────────────┐
        │                           │
        │                    Sources Provided?
        │                           │
        │                   Yes ────┘
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
                     END
```

---

# Graph Components

## State

The graph maintains a single Shared State that is updated throughout the workflow.

The state contains:

- Claim
- Sources
- Source Types
- Trust Scores
- Verification Result
- Confidence Score
- Workflow Status
- Execution Logs

---

## Nodes

Every specialized agent is represented as a LangGraph node.

| Node | Description |
|------|-------------|
| START | Entry point of the workflow |
| Coordinator | Controls workflow execution |
| Search | Retrieves evidence |
| Source Classification | Classifies evidence sources |
| Trust | Evaluates source credibility |
| Verification | Determines claim validity |
| Confidence | Calculates confidence score |
| END | Returns final response |

---

# Node Responsibilities

## START

Receives the incoming request.

↓

Passes control to the Coordinator Agent.

---

## Coordinator Agent

Responsibilities:

- Analyze request
- Select workflow
- Route execution
- Maintain workflow status
- Aggregate results

The Coordinator determines whether certain agents should be skipped.

---

## Search Agent

Responsibilities:

- Generate search queries
- Retrieve evidence
- Filter search results
- Store sources in Shared State

---

## Source Classification Agent

Responsibilities:

- Analyze retrieved sources
- Identify source type
- Store classifications

Possible classifications:

- Official
- Research
- Government
- News
- Technical
- Organization
- Community
- Personal

---

## Trust Agent

Responsibilities:

- Evaluate source credibility
- Assign trust scores
- Explain trust decisions

Trust Scale

```
1 – 10
```

---

## Verification Agent

Responsibilities:

- Analyze evidence
- Consider trust scores
- Determine factual validity

Possible verdicts

```
SUPPORTED

UNSUPPORTED

PARTIALLY_SUPPORTED

UNKNOWN
```

---

## Confidence Agent

Responsibilities:

Calculate confidence using:

- Trust scores
- Evidence count
- Source agreement
- Contradictions
- Source diversity

Confidence Scale

```
0 – 100
```

---

## END

Returns the completed verification response.

---

# Graph Edges

Edges define the execution order between nodes.

Main workflow

```text
START

↓

Coordinator

↓

Search

↓

Source Classification

↓

Trust

↓

Verification

↓

Confidence

↓

Coordinator

↓

END
```

---

# Conditional Routing

The Coordinator dynamically selects the execution path.

---

## Workflow A

Verify a claim

```text
START

↓

Coordinator

↓

Search

↓

Source Classification

↓

Trust

↓

Verification

↓

Confidence

↓

END
```

---

## Workflow B

Verify with user-provided sources

```text
START

↓

Coordinator

↓

Source Classification

↓

Trust

↓

Verification

↓

Confidence

↓

END
```

The Search Agent is skipped because evidence is already available.

---

## Workflow C

Evaluate source trust

```text
START

↓

Coordinator

↓

Source Classification

↓

Trust

↓

END
```

Verification and Confidence Agents are not required.

---

## Workflow D

Evidence search only

```text
START

↓

Coordinator

↓

Search

↓

END
```

---

# Shared State Flow

Every node interacts with the Shared State.

```text
Coordinator

↓

Shared State

↓

Search Agent

↓

Shared State

↓

Source Classification Agent

↓

Shared State

↓

Trust Agent

↓

Shared State

↓

Verification Agent

↓

Shared State

↓

Confidence Agent

↓

Shared State

↓

Coordinator
```

Each node:

- Reads required data
- Processes the task
- Writes owned data
- Updates execution status
- Writes execution logs

---

# Workflow Lifecycle

Every node follows the same lifecycle.

```text
Receive Task

↓

Read Shared State

↓

Execute Task

↓

Update Shared State

↓

Write Execution Log

↓

Update Agent Status

↓

Return Control
```

---

# Dynamic Decision Making

The Coordinator performs intelligent routing.

Examples:

### Claim only

```
Search required
```

---

### Sources already provided

```
Skip Search Agent
```

---

### Trust evaluation request

```
Skip Verification
Skip Confidence
```

---

### Evidence retrieval request

```
Search only
```

---

# Benefits

Using LangGraph provides:

- Stateful execution
- Dynamic workflows
- Modular architecture
- Reusable agents
- Centralized orchestration
- Easy debugging
- Workflow visualization
- Scalable design
- Future extensibility

---

# Future Enhancements

The graph can be extended by adding new nodes without changing the overall architecture.

Possible future nodes include:

- Citation Agent
- Explainability Agent
- Bias Detection Agent
- Hallucination Detection Agent
- Risk Assessment Agent
- Translation Agent
- Summarization Agent

The Coordinator can dynamically include these nodes based on user requests.

---

# LangGraph Mapping

| LangGraph Concept | EcoVerify Component |
|-------------------|---------------------|
| State | Shared State |
| Node | AI Agent |
| Edge | Agent Communication |
| Conditional Edge | Coordinator Decision |
| START | Workflow Entry |
| END | Final Response |
| StateGraph | EcoVerify Workflow |
| Router | Coordinator Agent |

---

# Conclusion

The EcoVerify Agent Ecosystem maps naturally to LangGraph by representing each specialized AI agent as a node within a shared state workflow. The Coordinator Agent manages routing through conditional edges, allowing the system to execute only the agents required for a particular request.

This architecture provides a scalable, maintainable, and production-ready foundation for building a composable multi-agent verification system compatible with the CROO Agent Protocol (CAP).