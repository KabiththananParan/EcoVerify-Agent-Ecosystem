from dataclasses import dataclass

@dataclass
class Source():
    url: str 
    title: str | None = None
    content: str | None = None
    publisher: str | None = None
    source_type: str | None = None
    trust_score: int | None = None