from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QToolBar, QAction, QTextEdit, QDockWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from llm_client import get_summary, get_simplified
from PyQt5.QtGui import QIcon

class LensBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))
        self.setCentralWidget(self.browser)

        navtb = QToolBar()
        self.addToolBar(navtb)
        
        # Navigation
        navtb.addAction(self.create_nav_action("Back", self.browser.back,"assets/icons/arrow-left-s-fill.svg"))
        navtb.addAction(self.create_nav_action("Forward", self.browser.forward, "assets/icons/arrow-right-s-fill.svg"))
        navtb.addAction(self.create_nav_action("Reload", self.browser.reload, "assets/icons/reload.svg"))
        navtb.addAction(self.create_nav_action("Home", self.navigate_home, "assets/icons/home.svg"))

        # URL bar
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)

        # Gemini Features
        insight_btn = QAction("Insight Mode", self)
        insight_btn.triggered.connect(self.insight_mode)
        navtb.addAction(insight_btn)

        simplify_btn = QAction("Simplify", self)
        simplify_btn.triggered.connect(self.simplify_mode)
        navtb.addAction(simplify_btn)

        self.summary_dock = QDockWidget("Lens Insight", self)
        self.summary_box = QTextEdit()
        self.summary_box.setReadOnly(True)
        self.summary_dock.setWidget(self.summary_box)
        self.addDockWidget(2, self.summary_dock)  # Right

        self.browser.urlChanged.connect(self.update_urlbar)
        self.show()

    # def create_nav_action(self, name, func):
    #     action = QAction(name, self)
    #     action.triggered.connect(func)
    #     return action
    
    def create_nav_action(self, name, func, icon_path=None):
        if icon_path:
            icon = QIcon(icon_path)
            action = QAction(icon, name, self)
        else:
            action = QAction(name, self)
        action.triggered.connect(func)
        return action

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.urlbar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, qurl):
        self.urlbar.setText(qurl.toString())

    def insight_mode(self):
        def handle_text(text):
            self.summary_box.setPlainText("Summarizing... Please wait.")
            summary = get_summary(text)
            self.summary_box.setPlainText(summary)
        self.browser.page().toPlainText(handle_text)

    def simplify_mode(self):
        def handle_text(text):
            self.summary_box.setPlainText("Simplifying... Please wait.")
            simplified = get_simplified(text)
            self.summary_box.setPlainText(simplified)
        self.browser.page().toPlainText(handle_text)

from extract import extract_visible_text

def insight_mode(self):
    def handle_text(text):
        self.summary_box.setPlainText("Summarizing... Please wait.")
        summary = get_summary(text)
        self.summary_box.setPlainText(summary)
    extract_visible_text(self.browser.page(), handle_text)
