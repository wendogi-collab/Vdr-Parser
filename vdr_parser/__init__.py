"""VDR parser package for extracting file references and exporting them to XLSX."""

from .models import DocumentRecord
from .path_parser import parse_vdr_path

__all__ = ["DocumentRecord", "parse_vdr_path"]
