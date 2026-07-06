# Source Classification Agent

## Overview

The Source Classification Agent is responsible for identifying the type of each retrieved source. It analyzes source metadata, URLs, domains, and content to classify sources into predefined categories.

The Source Classification Agent does not evaluate trustworthiness or determine factual correctness. Its sole responsibility is source categorization.

---

# Purpose

To classify evidence sources into predefined source categories.

---

# Agent Type

```
Intelligent Stateful Classification Agent
```

---

# Responsibilities

### 1. Receive Sources

Accept sources from the Coordinator Agent.

Example:

```json
{
    "title": "AWS Documentation",
    "url": "https://aws.amazon.com/lambda/snapstart/"
}
```

---

### 2. Analyze Source Information

Analyze:

- Domain
- URL structure
- Website metadata
- Publisher
- Content patterns

---

### 3. Perform Classification Reasoning

Determine the most appropriate source category.

Example:

```
aws.amazon.com
        ↓
Official company documentation
        ↓
official
```

---

### 4. Return Source Category

Return structured classification results.

---

# Source Categories

```
official
research
government
news
technical
organization
community
personal
```

---

# Input

```json
{
    "title": "string",
    "url": "string",
    "content": "string"
}
```

---

# Workflow State

Example:

```json
{
    "sources_processed": 5,
    "official": 2,
    "research": 1,
    "news": 1,
    "community": 1,
    "status": "completed"
}
```

---

# Output

```json
{
    "source_type": "string"
}
```

---

# Example Output

```json
{
    "source_type": "official"
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

- Determine publisher type
- Analyze domains
- Infer source category
- Resolve ambiguous sources

---

# Does This Agent Maintain State?

```
YES
```

Reasons:

- Workflow tracking
- Debugging
- Retry support
- Statistics
- Visualization

---

# What This Agent Does NOT Do

The Source Classification Agent does NOT:

- Calculate trust scores
- Verify claims
- Calculate confidence
- Determine factual correctness

---

# Skills Learned Through This Agent

- Source analysis
- Classification systems
- AI reasoning
- Metadata analysis
- Information categorization
- State management
- Multi-agent communication