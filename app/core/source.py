from dataclasses import dataclass

@dataclass
class Source():
    title: str
    url: str
    content: str
    publisher: str
    source_type: str | None = None
    trust_score: int | None = None