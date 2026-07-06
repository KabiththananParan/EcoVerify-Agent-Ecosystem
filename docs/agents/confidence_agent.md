# Confidence Agent

## Overview

The Confidence Agent is responsible for estimating the certainty of the verification result. It analyzes trust scores, evidence quantity, source agreement, contradictions, and source diversity to produce a confidence score.

The Confidence Agent does not determine whether a claim is true or false. Its sole responsibility is estimating confidence in the verification result.

---

# Purpose

To calculate the certainty of the verification result.

---

# Agent Type

```
Intelligent Stateful Confidence Estimation Agent
```

---

# Responsibilities

### 1. Receive Verification Results

Accept:

- Verification verdict
- Trust scores
- Evidence statistics
- Agreement metrics
- Contradiction metrics

---

### 2. Analyze Confidence Factors

Evaluate:

- Source trust scores
- Evidence count
- Source agreement
- Contradictions
- Source diversity

---

### 3. Perform Confidence Reasoning

Examples:

```
High trust
+
Many sources
+
Strong agreement
+
No contradictions
=
High confidence
```

---

### 4. Calculate Confidence Score

Produce a confidence score between:

```
0 - 100
```

---

### 5. Return Confidence Result

Return:

- Confidence score
- Explanation

---

# Confidence Factors

- Trust scores
- Evidence count
- Source agreement
- Contradictions
- Source diversity

---

# Input

```json
{
    "verdict":"SUPPORTED",

    "trust_scores":[10,9,10],

    "evidence_count":3,

    "agreement":100,

    "contradictions":0,

    "source_diversity":3
}
```

---

# Workflow State

Example:

```json
{
    "verdict":"SUPPORTED",

    "average_trust":9.6,

    "evidence_count":3,

    "agreement":100,

    "contradictions":0,

    "status":"completed"
}
```

---

# Output

```json
{
    "confidence":97,

    "reason":
        "Multiple highly trusted and diverse sources agree."
}
```

---

# Example Output

```json
{
    "confidence":97,

    "reason":
        "Three highly trusted sources consistently support the claim."
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

- Evaluate certainty
- Analyze contradictions
- Assess evidence strength
- Estimate confidence

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

The Confidence Agent does NOT:

- Search evidence
- Classify sources
- Calculate trust scores
- Verify claims

---

# Skills Learned Through This Agent

- Confidence estimation
- Uncertainty analysis
- AI reasoning
- Trust aggregation
- Multi-agent systems
- State management