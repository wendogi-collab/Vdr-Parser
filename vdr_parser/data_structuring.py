from .models import DocumentRecord
from .path_parser import parse_vdr_path


def structure_records(raw_records: list[dict]) -> list[DocumentRecord]:
    """Convert raw scraped metadata dictionaries into structured records."""
    structured: list[DocumentRecord] = []
    for item in raw_records:
        raw_path = item.get("folder_path", "")
        document_name = item.get("document_name", "")
        hierarchy = parse_vdr_path(raw_path)

        # Ensure filename is captured in hierarchy if not present.
        if document_name and (not hierarchy or hierarchy[-1] != document_name):
            hierarchy = [*hierarchy, document_name]

        structured.append(
            DocumentRecord(
                unique_id=str(item.get("unique_id", "")),
                document_name=document_name,
                raw_path=raw_path,
                hierarchy=hierarchy,
            )
        )
    return structured
