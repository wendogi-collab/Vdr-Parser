from dataclasses import dataclass, field


@dataclass
class DocumentRecord:
    """Structured representation of one VDR document reference."""

    unique_id: str
    document_name: str
    raw_path: str
    hierarchy: list[str] = field(default_factory=list)

    @property
    def normalized_path(self) -> str:
        return " > ".join(self.hierarchy)
