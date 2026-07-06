# Trust Agent

## Overview

The Trust Agent is responsible for evaluating the trustworthiness and credibility of classified sources. It analyzes source categories, domains, publishers, and source characteristics to assign a trust score and provide reasoning for the assigned score.

The Trust Agent does not verify claims or calculate confidence. Its sole responsibility is evaluating source credibility.

---

# Purpose

To determine how trustworthy a source is.

---

# Agent Type

```
Intelligent Stateful Evaluation Agent
```

---

# Responsibilities

### 1. Receive Classified Source

Accept classified sources from the Coordinator Agent.

Example:

```json
{
    "title": "AWS Documentation",
    "url": "https://aws.amazon.com/",
    "source_type": "official"
}
```

---

### 2. Analyze Source Credibility

Evaluate:

- Source category
- Domain reputation
- Publisher reputation
- Information quality
- Source authority

---

### 3. Perform Trust Reasoning

Examples:

```
AWS Documentation
        ↓
Official company documentation
        ↓
Highly authoritative
        ↓
Trust Score = 10
```

---

### 4. Return Trust Score

Return a trust score and explanation.

---

# Trust Scale

| Score | Meaning |
|-------|---------|
| 10 | Highly trustworthy |
| 8-9 | Very trustworthy |
| 6-7 | Moderately trustworthy |
| 4-5 | Low trust |
| 2-3 | Very low trust |
| 1 | Untrusted |

---

# Input

```json
{
    "title": "string",
    "url": "string",
    "source_type": "string"
}
```

---

# Workflow State

Example:

```json
{
    "sources_processed": 5,
    "average_trust": 8.4,
    "highest_trust": 10,
    "lowest_trust": 3,
    "status": "completed"
}
```

---

# Output

```json
{
    "trust_score": 10,
    "reason": "Official documentation from AWS."
}
```

---

# Example Output

```json
{
    "trust_score": 10,
    "reason": "Source is official documentation published by AWS."
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

- Evaluate source authority
- Compare source reliability
- Infer source credibility
- Analyze publisher reputation

---

# Does This Agent Maintain State?

```
YES
```

Reasons:

- Workflow tracking
- Debugging
- Statistics
- Retry support
- Visualization

---

# What This Agent Does NOT Do

The Trust Agent does NOT:

- Verify claims
- Calculate confidence
- Determine factual correctness
- Search for evidence

---

# Skills Learned Through This Agent

- Trust evaluation systems
- Credibility analysis
- AI reasoning
- Source reliability assessment
- State management
- Multi-agent communication
