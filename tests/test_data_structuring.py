from vdr_parser.data_structuring import structure_records


def test_structure_records_appends_doc_name_when_missing_from_path():
    raw = [
        {
            "unique_id": "A-001",
            "document_name": "Contract 1",
            "folder_path": "Corporate > Employment > Employment Contracts",
        }
    ]

    records = structure_records(raw)

    assert len(records) == 1
    assert records[0].normalized_path == (
        "Corporate > Employment > Employment Contracts > Contract 1"
    )
