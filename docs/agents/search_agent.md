# Search Agent

## Overview

The Search Agent is responsible for discovering relevant evidence related to a given claim. It performs intelligent search query generation, retrieves evidence from multiple sources, maintains search state, and returns structured evidence to the Coordinator Agent.

The Search Agent does not determine whether a claim is true or false. Its only responsibility is evidence retrieval.

---

# Purpose

To find relevant evidence, articles, documents, and sources related to a claim.

---

# Agent Type

```
Intelligent Stateful Retrieval Agent
```

---

# Responsibilities

### 1. Receive Claim

Accept a claim from the Coordinator Agent.

Example:

```json
{
    "claim": "AWS SnapStart reduces Lambda cold starts"
}
```

---

### 2. Perform Search Reasoning

Generate optimized search queries from the claim.

Example:

Claim:

```
AWS SnapStart reduces Lambda cold starts
```

Generated queries:

```
AWS Lambda SnapStart official documentation
AWS SnapStart performance benchmarks
AWS SnapStart research paper
AWS SnapStart AWS blog
```

---

### 3. Search Multiple Sources

Retrieve evidence from available sources such as:

- Official documentation
- Research papers
- News articles
- Technical blogs
- Government websites
- Community sources

---

### 4. Filter Results

Remove:

- Duplicate sources
- Broken links
- Irrelevant results
- Low-quality results

---

### 5. Return Structured Evidence

Prepare structured evidence for downstream agents.

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
    "max_results": 10
}
```

---

# Workflow State

Example:

```json
{
    "claim":
        "AWS SnapStart reduces Lambda cold starts",

    "generated_queries":
    [
        "AWS Lambda SnapStart official documentation",
        "AWS SnapStart performance benchmark"
    ],

    "results_found": 15,

    "selected_results": 5,

    "status": "completed"
}
```

---

# Output

```json
{
    "sources":
    [
        {
            "title": "string",
            "url": "string",
            "content": "string"
        }
    ]
}
```

---

# Example Output

```json
{
    "sources":
    [
        {
            "title": "AWS Documentation",
            "url": "https://aws.amazon.com/lambda/snapstart/",
            "content":
                "AWS Lambda SnapStart improves startup performance..."
        },

        {
            "title": "AWS Blog",
            "url": "https://aws.amazon.com/blogs/",
            "content":
                "SnapStart significantly reduces cold start latency..."
        }
    ]
}
```

---

# Called By

- Coordinator Agent

---

# Does This Agent Perform AI Reasoning?

```
YES
```

Examples:

- Generate better search queries
- Select relevant search terms
- Optimize retrieval strategy
- Determine search priorities

---

# Does This Agent Maintain State?

```
YES
```

Reasons:

- Workflow tracking
- Debugging
- Retry support
- Result caching
- Visualization

---

# What This Agent Does NOT Do

The Search Agent does NOT:

- Classify sources
- Calculate trust scores
- Verify claims
- Calculate confidence
- Make factual judgments

---

# Skills Learned Through This Agent

- Information retrieval
- Search optimization
- Query generation
- Retrieval systems
- State management
- Agent reasoning
- Evidence collection
- Multi-agent communication