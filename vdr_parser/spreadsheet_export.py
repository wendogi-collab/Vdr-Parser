from openpyxl import Workbook

from .models import DocumentRecord


def export_to_xlsx(records: list[DocumentRecord], output_file: str) -> None:
    """Export structured document references into an XLSX spreadsheet."""
    wb = Workbook()
    ws = wb.active
    ws.title = "VDR References"

    ws.append(["Unique ID", "Document Name", "Raw Folder Path", "Normalized Reference"])

    for record in records:
        ws.append(
            [
                record.unique_id,
                record.document_name,
                record.raw_path,
                record.normalized_path,
            ]
        )

    wb.save(output_file)
