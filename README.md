# Vdr-Parser

A Python-based plugin-style toolchain to extract document references from a Virtual Data Room (VDR), normalize the folder path hierarchy, and export results into `.xlsx` for legal due diligence workflows.

## What it does

The project is organized into modules that mirror your intended architecture:

- **Metadata fetch module** (`metadata_fetcher.py`)
  - Runs an automated Playwright browser session.
  - Reads metadata from DOM elements (document name, folder path, unique ID).
- **Path extraction parser** (`path_parser.py`)
  - Splits folder paths into hierarchy segments.
  - Normalizes delimiters like `>`, `/`, `\\`, `→`, and `›`.
- **Data structuring layer** (`data_structuring.py`)
  - Converts raw metadata into strongly-typed records.
  - Ensures the document name is part of the final reference hierarchy.
- **Spreadsheet export module** (`spreadsheet_export.py`)
  - Exports references to an `.xlsx` file.

## Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
playwright install chromium
```

## Usage

### Option 1: Live VDR extraction via browser DOM

```bash
vdr-parser \
  --url "https://your-vdr.example/documents" \
  --output "vdr_references.xlsx"
```

Default selectors assume attributes on each document row:

- Row: `[data-doc-row]`
- Name: `[data-doc-name]`
- Path: `[data-folder-path]`
- ID: `[data-doc-id]`

Override selectors if your VDR uses different DOM markers:

```bash
vdr-parser \
  --url "https://your-vdr.example/documents" \
  --row-selector ".doc-row" \
  --name-selector ".doc-name" \
  --path-selector ".folder-path" \
  --id-selector ".doc-id" \
  --output "vdr_references.xlsx"
```

### Option 2: JSON input (offline / testing mode)

```bash
vdr-parser \
  --input-json sample_records.json \
  --output vdr_references.xlsx
```

`sample_records.json` format:

```json
[
  {
    "unique_id": "A-001",
    "document_name": "Contract 1",
    "folder_path": "Corporate > Employment > Employment Contracts"
  }
]
```

Output normalized reference example:

`Corporate > Employment > Employment Contracts > Contract 1`

## Running tests

```bash
pytest
```
