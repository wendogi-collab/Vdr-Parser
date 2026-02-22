from vdr_parser.path_parser import parse_vdr_path


def test_parse_vdr_path_with_mixed_delimiters():
    raw = "Corporate > Employment / Employment Contracts \\ Contract 1"
    assert parse_vdr_path(raw) == [
        "Corporate",
        "Employment",
        "Employment Contracts",
        "Contract 1",
    ]
