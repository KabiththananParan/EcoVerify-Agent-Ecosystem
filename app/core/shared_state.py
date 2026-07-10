from dataclasses import dataclass, field
from source import Source

@dataclass
class SharedState():
    claim: str
    sources: list[Source] = field(default_factory=list)
    verification_result: str | None = None # Verification Agent
    verification_reason: str | None = None
    confidence_score: int | None = None # Confidence Agent
    workflow_status: str = "Pending" # Coordinator
    logs: list[str] = field(default_factory=list) # Logging