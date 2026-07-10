# Error Handling

## Overview

The EcoVerify Agent Ecosystem is designed to handle failures gracefully without unnecessarily terminating the entire workflow. Since multiple AI agents collaborate to complete a verification request, each agent is responsible for reporting errors while the **Coordinator Agent** is responsible for deciding how the workflow should proceed.

This architecture improves reliability, debugging, and fault tolerance.

---

# Error Handling Architecture

```text
                   Coordinator Agent
                          │
        ┌─────────────────┼─────────────────┐
        ▼                 ▼                 ▼
   Search Agent      Trust Agent     Verification Agent
        │                 │                 │
        └──────────── Error ────────────────┘
                          │
                          ▼
                 Error Recovery Decision
                          │
          ┌───────────────┼───────────────┐
          ▼               ▼               ▼
       Retry          Continue        Stop Workflow
```

---

# Error Handling Principles

The EcoVerify ecosystem follows these principles:

- Every agent is responsible for detecting its own errors.
- Every agent reports errors using a standard format.
- Every agent records execution logs.
- The Coordinator decides how to recover.
- Recoverable errors should not terminate the workflow.
- Critical failures stop the workflow.

---

# Error Lifecycle

Every agent follows the same lifecycle.

```text
Receive Task
      │
      ▼
Execute Task
      │
      ▼
Task Successful?
      │
 ┌────┴────┐
 │         │
Yes        No
 │         │
 ▼         ▼
Update     Report Error
State      Write Log
 │         │
 ▼         ▼
Return   Coordinator
```

---

# Standard Error Format

Every agent reports errors using the same structure.

```json
{
    "agent": "Search Agent",
    "status": "Failed",
    "error_code": "SEARCH_TIMEOUT",
    "reason": "Search request timed out."
}
```

---

# Agent Status

Each agent maintains its own execution status.

Possible values

```
Pending

Running

Completed

Retrying

Skipped

Failed
```

The Coordinator monitors the status of all agents to determine the overall workflow status.

---

# Error Types

## 1. Search Agent Errors

Possible errors

- Search timeout
- Network failure
- Search API unavailable
- Rate limit exceeded
- No search results

Recovery

```
Retry once

↓

Use fallback search

↓

Return empty result

↓

Continue workflow
```

---

## 2. Source Classification Errors

Possible errors

- Invalid URL
- Unknown website
- Unsupported source

Recovery

Assign

```text
source_type = unknown
```

Continue workflow.

---

## 3. Trust Agent Errors

Possible errors

- Unable to determine credibility
- Unknown publisher
- Missing metadata

Recovery

Assign

```text
trust_score = 1
```

Reason

```
Unable to evaluate source credibility.
```

Continue workflow.

---

## 4. Verification Agent Errors

Possible errors

- LLM timeout
- Parsing failure
- Missing evidence
- Invalid response

Recovery

```
Retry

↓

UNKNOWN verdict

↓

Continue workflow
```

---

## 5. Confidence Agent Errors

Possible errors

- Missing trust scores
- Missing verdict
- Calculation failure

Recovery

Assign

```text
confidence = 0
```

Reason

```
Unable to estimate confidence.
```

Continue workflow.

---

## 6. Coordinator Agent Errors

Possible errors

- Invalid request
- Unsupported task
- Missing input

Recovery

Return validation error immediately.

Example

```json
{
    "status": "Failed",
    "reason": "Claim is required."
}
```

---

## 7. CAP Integration Errors

Possible errors

- Payment failed
- Authentication failed
- Agent unavailable
- Invalid request

Recovery

Workflow does not start.

Return

```json
{
    "status": "Failed",
    "reason": "Payment verification failed."
}
```

---

# Retry Strategy

The Coordinator decides how to recover.

Possible strategies

```
Retry Once

↓

Retry Using Backup Service

↓

Skip Agent

↓

Stop Workflow
```

Each retry attempt is logged.

---

# Execution Logs

Every agent records execution logs.

Example

```json
{
    "agent": "Search Agent",
    "level": "INFO",
    "message": "Started search."
}
```

```json
{
    "agent": "Search Agent",
    "level": "INFO",
    "message": "Retrieved 5 sources."
}
```

```json
{
    "agent": "Trust Agent",
    "level": "WARNING",
    "message": "Unknown publisher detected."
}
```

```json
{
    "agent": "Verification Agent",
    "level": "ERROR",
    "message": "LLM timeout."
}
```

Logs are stored in the Shared State.

---

# Workflow Recovery Examples

## Example 1

Search timeout

```text
Search Agent

↓

Timeout

↓

Retry

↓

Success

↓

Continue
```

---

## Example 2

Unknown website

```text
Source Classification

↓

Unknown Domain

↓

Classify as Unknown

↓

Continue
```

---

## Example 3

Trust evaluation failed

```text
Trust Agent

↓

Unknown Publisher

↓

Trust Score = 1

↓

Continue
```

---

## Example 4

Verification timeout

```text
Verification Agent

↓

LLM Timeout

↓

Retry

↓

Still Failed

↓

Verdict = UNKNOWN

↓

Continue
```

---

## Example 5

CAP payment failure

```text
Payment Failed

↓

Coordinator

↓

Workflow Terminated
```

---

# Error Severity Levels

| Level | Meaning | Action |
|---------|---------|--------|
| INFO | Normal operation | Continue |
| WARNING | Recoverable issue | Continue with fallback |
| ERROR | Task failure | Retry or fallback |
| CRITICAL | Workflow cannot continue | Stop workflow |

---

# Coordinator Responsibilities

The Coordinator Agent is responsible for:

- Receiving all error reports
- Monitoring workflow status
- Selecting recovery strategies
- Updating workflow state
- Returning user-friendly error responses

The Coordinator does **not** attempt to fix errors itself. It decides how the workflow should proceed.

---

# Benefits

This error handling architecture provides:

- Fault tolerance
- Graceful recovery
- Consistent error reporting
- Easier debugging
- Better observability
- Reliable workflow execution
- Production-ready architecture

---

# Future Enhancements

Future versions of EcoVerify may include:

- Automatic exponential backoff retries
- Circuit breaker pattern
- Multiple search provider failover
- LLM provider failover
- Distributed tracing
- Real-time monitoring dashboard
- Alerting and notification system
- Error analytics

These enhancements can be added without changing the overall error handling architecture.

---

# Conclusion

The EcoVerify Agent Ecosystem uses centralized error management where each specialized agent reports failures and the Coordinator Agent determines the appropriate recovery strategy. This approach keeps the system resilient, modular, and maintainable while ensuring that recoverable failures do not unnecessarily terminate the verification workflow.