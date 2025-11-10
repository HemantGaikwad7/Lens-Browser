# extract.py

"""
Extraction utilities for Lens Browser.
Extracts visible text from QWebEnginePage.
Can be expanded to add advanced parsing features (HTML structure, meta tags, etc.)
"""

from PyQt5.QtWebEngineWidgets import QWebEnginePage

def extract_visible_text(page: QWebEnginePage, callback):
    """
    Extract visible, rendered text from a QWebEnginePage.
    - page: QWebEnginePage object (use .page() on QWebEngineView)
    - callback: function that receives the extracted text (async pattern)
    """
    if not isinstance(page, QWebEnginePage):
        raise ValueError("page must be a QWebEnginePage")
    # Asynchronous: will call callback(text) when ready
    page.toPlainText(callback)

# (Optional future functions:)
def extract_html(page: QWebEnginePage, callback):
    """
    Extracts raw HTML of the current page.
    Calls callback(html_str) when done.
    """
    page.toHtml(callback)

# Example for later:
# def extract_metadata(page: QWebEnginePage, callback):
#     # Could use JavaScript eval to extract <title>, <meta>, etc.
#     pass
