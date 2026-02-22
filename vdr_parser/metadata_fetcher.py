from dataclasses import dataclass

from playwright.sync_api import sync_playwright


@dataclass
class DOMSelectors:
    row: str = "[data-doc-row]"
    name: str = "[data-doc-name]"
    path: str = "[data-folder-path]"
    unique_id: str = "[data-doc-id]"


def fetch_metadata(url: str, selectors: DOMSelectors, headless: bool = True) -> list[dict]:
    """
    Launch browser, read metadata from DOM rows and return document metadata.

    Expected schema per row:
      - data-doc-name
      - data-folder-path
      - data-doc-id
    """
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=headless)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        rows = page.locator(selectors.row)
        results: list[dict] = []

        for i in range(rows.count()):
            row = rows.nth(i)
            results.append(
                {
                    "document_name": row.locator(selectors.name).inner_text().strip(),
                    "folder_path": row.locator(selectors.path).inner_text().strip(),
                    "unique_id": row.locator(selectors.unique_id).inner_text().strip(),
                }
            )

        browser.close()
        return results
