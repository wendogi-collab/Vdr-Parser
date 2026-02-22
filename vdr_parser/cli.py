import argparse
import json

from .data_structuring import structure_records
from .metadata_fetcher import DOMSelectors, fetch_metadata
from .spreadsheet_export import export_to_xlsx


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Extract VDR document paths and export reference numbers to XLSX."
    )
    parser.add_argument("--url", help="VDR listing URL for browser extraction")
    parser.add_argument(
        "--input-json",
        help="Path to JSON array of objects with keys: document_name, folder_path, unique_id",
    )
    parser.add_argument("--output", required=True, help="Output XLSX file path")
    parser.add_argument("--headed", action="store_true", help="Run browser with visible UI")
    parser.add_argument("--row-selector", default="[data-doc-row]")
    parser.add_argument("--name-selector", default="[data-doc-name]")
    parser.add_argument("--path-selector", default="[data-folder-path]")
    parser.add_argument("--id-selector", default="[data-doc-id]")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if not args.url and not args.input_json:
        raise SystemExit("Provide either --url for browser extraction or --input-json.")

    if args.input_json:
        with open(args.input_json, "r", encoding="utf-8") as f:
            raw_records = json.load(f)
    else:
        selectors = DOMSelectors(
            row=args.row_selector,
            name=args.name_selector,
            path=args.path_selector,
            unique_id=args.id_selector,
        )
        raw_records = fetch_metadata(args.url, selectors=selectors, headless=not args.headed)

    records = structure_records(raw_records)
    export_to_xlsx(records, args.output)
    print(f"Exported {len(records)} records to {args.output}")


if __name__ == "__main__":
    main()
