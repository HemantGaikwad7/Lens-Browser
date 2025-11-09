# 🔍 LensBrowser - AI-Powered Web Browser

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/PyQt5-5.15+-green.svg" alt="PyQt5">
  <img src="https://img.shields.io/badge/AI-Gemini%20%7C%20OpenAI-orange.svg" alt="AI Models">
</p>

A lightweight, AI-enhanced web browser built with PyQt5 that can summarize, rewrite, and extract insights from web content in real-time.

## ✨ Features

- 🌐 **Full Web Browsing**: Complete web browser functionality with navigation controls
- 📝 **Smart Summarization**: Generate TL;DR summaries of any webpage
- ✏️ **Content Rewriting**: Rewrite content for better readability
- 💡 **Insight Extraction**: Extract key insights, action items, and important facts
- 📄 **Text Extraction**: Extract clean, visible text from any webpage
- 🎯 **Side Panel Interface**: Non-intrusive AI insights panel
- ⌨️ **Keyboard Shortcuts**: Efficient navigation and AI features
- 🔄 **Multiple AI Providers**: Support for both Gemini and OpenAI APIs

## 📸 Screenshots

```
┌─────────────────────────────────────────────────────────────┐
│  ← Back | Forward → | ⟳ Reload | 🏠 Home | [URL Bar.......]  │
│  📝 Summarize | 💡 Insights | ✏️ Rewrite | 📄 Extract Text   │
├──────────────────────────────────┬──────────────────────────┤
│                                  │   AI Insights            │
│   Web Content Area               │  ┌──────────────────┐    │
│                                  │  │ Summary          │    │
│   [Webpage renders here]         │  │ Extracted Text   │    │
│                                  │  │ Rewritten        │    │
│                                  │  │ Insights         │    │
│                                  │  └──────────────────┘    │
│                                  │  [Content displays here] │
│                                  │  📋 Copy | 🗑️ Clear     │
└──────────────────────────────────┴──────────────────────────┘
```

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager
- API key from Google (Gemini) or OpenAI

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/LensBrowser.git
cd LensBrowser
```

2. **Create virtual environment**
```bash
python -m venv venv

# Activate it:
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up API keys**

Create a `.env` file in the project root:

```bash
# Copy the example file
cp .env.example .env

# Edit .env and add your API keys:
GEMINI_API_KEY=your_gemini_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
DEFAULT_LLM_PROVIDER=gemini
DEFAULT_HOME_PAGE=https://www.google.com
```

**Get API Keys:**
- **Gemini**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenAI**: Visit [OpenAI Platform](https://platform.openai.com/api-keys)

5. **Run the browser**
```bash
python src/main.py
```

## ⌨️ Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+L` | Focus URL bar |
| `Ctrl+S` | Summarize current page |
| `Ctrl+I` | Toggle insights panel |
| `Ctrl+R` | Reload page |
| `Alt+←` | Go back |
| `Alt+→` | Go forward |

## 🎯 Usage Examples

### 1. Summarize an Article

1. Navigate to any article or blog post
2. Click "📝 Summarize" or press `Ctrl+S`
3. View the TL;DR summary in the insights panel

### 2. Extract Clean Text

1. Visit any webpage
2. Click "📄 Extract Text"
3. Get clean, readable text without ads or navigation

### 3. Rewrite for Readability

1. Open a complex technical article
2. Click "✏️ Rewrite"
3. Get a more readable version of the content

### 4. Get Key Insights

1. Read any article
2. Click "💡 Insights"
3. View key takeaways, action items, and important facts

## 🏗️ Architecture

```
LensBrowser/
├── src/
│   ├── main.py              # Application entry point
│   ├── browser/
│   │   ├── window.py        # Main browser window
│   │   ├── web_view.py      # Custom web view
│   │   └── toolbar.py       # Navigation toolbar
│   ├── ai/
│   │   ├── llm_client.py    # Unified LLM API client
│   │   ├── summarizer.py    # Content summarization
│   │   └── rewriter.py      # Content rewriting
│   ├── ui/
│   │   ├── insight_panel.py # AI insights side panel
│   │   └── styles.py        # UI styling
│   └── utils/
│       ├── text_extractor.py # HTML text extraction
│       └── config.py         # Configuration management
```

## 🧪 Testing

Run tests with pytest:

```bash
# Install test dependencies
pip install pytest pytest-qt

# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

## 🔧 Configuration

Edit `config/settings.json` or `.env` to customize:

```json
{
  "browser": {
    "home_page": "https://www.google.com",
    "user_agent": "LensBrowser/1.0"
  },
  "ai": {
    "provider": "gemini",
    "max_tokens": 8000,
    "temperature": 0.7
  },
  "ui": {
    "theme": "light",
    "font_size": 12
  }
}
```

## 📊 Performance

- **Text Extraction**: ~100ms for typical webpage
- **Summarization**: 2-5 seconds (depends on content length and API)
- **Memory Usage**: ~150-200MB baseline
- **Supported Page Size**: Up to 32,000 tokens (~128KB text)

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 Development Roadmap

### Phase 1 (Current)
- [x] Basic browser functionality
- [x] Text extraction
- [x] LLM integration
- [x] Summarization
- [x] Insights panel

### Phase 2 (Next)
- [ ] Multi-tab support
- [ ] Bookmarks manager
- [ ] History tracking
- [ ] Download manager
- [ ] Dark mode

### Phase 3 (Future)
- [ ] Browser extensions support
- [ ] Sync across devices
- [ ] Collaborative features
- [ ] Voice reading of summaries
- [ ] Multi-language support

## 💡 Use Cases

1. **Research**: Quickly summarize academic papers and articles
2. **News Reading**: Get TL;DR of news articles
3. **Learning**: Simplify complex technical documentation
4. **Productivity**: Extract action items from blog posts
5. **Content Creation**: Rewrite content for different audiences

## 🎓 For Interview Preparation

This project demonstrates:

- **Software Architecture**: Clean separation of concerns, modular design
- **API Integration**: Working with external AI APIs
- **UI/UX Development**: PyQt5 desktop application development
- **Error Handling**: Robust error handling and user feedback
- **Testing**: Unit tests and integration tests
- **Documentation**: Comprehensive README and code comments
- **Configuration Management**: Environment variables and config files
- **Performance**: Async operations and optimization

### Talking Points for Interviews:

1. **Technical Challenges**: 
   - Extracting clean text from complex HTML
   - Managing API rate limits and costs
   - Handling large documents efficiently

2. **Design Decisions**:
   - Why PyQt5 over Electron
   - Choosing between Gemini and OpenAI
   - Architecture patterns used

3. **Scalability**:
   - How to add more AI features
   - Supporting multiple languages
   - Cloud deployment possibilities

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- PyQt5 for the UI framework
- Google Gemini for AI capabilities
- OpenAI for GPT models
- BeautifulSoup for HTML parsing

## 📧 Contact

Your Name - your.email@example.com

Project Link: [https://github.com/yourusername/LensBrowser](https://github.com/yourusername/LensBrowser)

---

**Note**: Remember to add your API keys to the `.env` file before running the application!
