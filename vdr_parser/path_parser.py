import re

PATH_SPLIT_PATTERN = re.compile(r"\s*(?:>|/|\\|→|›)\s*")


def parse_vdr_path(raw_path: str) -> list[str]:
    """Parse a raw VDR path into normalized hierarchy segments."""
    if not raw_path:
        return []

    cleaned = raw_path.strip()
    parts = [segment.strip() for segment in PATH_SPLIT_PATTERN.split(cleaned)]
    return [segment for segment in parts if segment]
