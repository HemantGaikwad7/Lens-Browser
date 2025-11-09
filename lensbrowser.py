from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QToolBar, QAction
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

class LensBrowser(QMainWindow):
    def __init__(self):
        super().__init__()

        # Browser widget to load and render web pages
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("http://www.google.com"))  # Default home page
        self.setCentralWidget(self.browser)

        # Navigation toolbar
        navtb = QToolBar()
        self.addToolBar(navtb)

        # Back button
        back_btn = QAction("Back", self)
        back_btn.triggered.connect(self.browser.back)
        navtb.addAction(back_btn)

        # Forward button
        forward_btn = QAction("Forward", self)
        forward_btn.triggered.connect(self.browser.forward)
        navtb.addAction(forward_btn)

        # Reload button
        reload_btn = QAction("Reload", self)
        reload_btn.triggered.connect(self.browser.reload)
        navtb.addAction(reload_btn)

        # Home button
        home_btn = QAction("Home", self)
        home_btn.triggered.connect(self.navigate_home)
        navtb.addAction(home_btn)

        # Address bar
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)  # Enter key triggers navigation
        navtb.addWidget(self.urlbar)

        # Update the URL bar when the browser navigates
        self.browser.urlChanged.connect(self.update_urlbar)

        self.show()

    def navigate_home(self):
        self.browser.setUrl(QUrl("http://www.google.com"))

    def navigate_to_url(self):
        url = self.urlbar.text()
        if not url.startswith("http"):
            url = "http://" + url
        self.browser.setUrl(QUrl(url))

    def update_urlbar(self, qurl):
        self.urlbar.setText(qurl.toString())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LensBrowser()
    sys.exit(app.exec_())