# Verification Agent

## Overview

The Verification Agent is responsible for determining whether the collected evidence supports, contradicts, partially supports, or cannot verify a claim. It performs reasoning over evidence while considering source trust scores.

The Verification Agent is the primary reasoning component of the EcoVerify Agent Ecosystem.

---

# Purpose

To determine the factual validity of a claim using trusted evidence.

---

# Agent Type

```
Intelligent Stateful Reasoning Agent
```

---

# Responsibilities

### 1. Receive Claim and Evidence

Accept:

- Claim
- Evidence
- Trust scores

Example:

```json
{
    "claim":
        "AWS SnapStart reduces Lambda cold starts",

    "evidence":
    [
        {
            "title":"AWS Documentation",
            "content":"...",
            "trust_score":10
        }
    ]
}
```

---

### 2. Analyze Evidence

Evaluate:

- Evidence consistency
- Contradictions
- Agreement
- Missing information
- Source reliability

---

### 3. Perform Verification Reasoning

Examples:

```
Evidence supports claim
        ↓
High trust sources
        ↓
SUPPORTED
```

or

```
Evidence conflicts
        ↓
Mixed support
        ↓
PARTIALLY_SUPPORTED
```

---

### 4. Consider Trust Scores

Higher trust sources have greater influence.

Example:

```
AWS Docs (10)
beats
Random Blog (2)
```

---

### 5. Return Verification Result

Return:

- Verdict
- Reasoning

---

# Verdict Categories

```
SUPPORTED
UNSUPPORTED
PARTIALLY_SUPPORTED
UNKNOWN
```

---

# Input

```json
{
    "claim":"string",

    "evidence":
    [
        {
            "title":"string",
            "content":"string",
            "trust_score":1
        }
    ]
}
```

---

# Workflow State

Example:

```json
{
    "claim_processed": true,
    "evidence_count": 5,
    "trusted_evidence": 3,
    "contradictions_found": 1,
    "status": "completed"
}
```

---

# Output

```json
{
    "verdict":"SUPPORTED",
    "reason":"Multiple trusted sources support the claim."
}
```

---

# Example Output

```json
{
    "verdict":"SUPPORTED",

    "reason":
        "Official documentation and research evidence support the claim."
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

- Analyze evidence
- Resolve contradictions
- Compare evidence quality
- Determine factual validity
- Weight evidence using trust scores

---

# Does This Agent Maintain State?

```
YES
```

Reasons:

- Workflow tracking
- Debugging
- Error recovery
- Visualization
- Statistics

---

# What This Agent Does NOT Do

The Verification Agent does NOT:

- Search for evidence
- Classify sources
- Calculate trust scores
- Calculate confidence

---

# Skills Learned Through This Agent

- Evidence reasoning
- Fact verification
- Contradiction analysis
- Trust-weighted reasoning
- Multi-agent systems
- AI reasoning
- State management