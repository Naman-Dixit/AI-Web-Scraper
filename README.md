# AI Web Scraper

A Streamlit web app that scrapes any website using Selenium and lets you extract specific information from the page content using a local LLM (Llama 3 via Ollama).

---

## How it works

1. Enter a URL — Selenium launches a Chrome browser, loads the page, and captures the full HTML.
2. The HTML is parsed with BeautifulSoup: scripts and styles are stripped, leaving clean readable text.
3. You describe what you want to extract in plain English.
4. The cleaned content is split into 6,000-character chunks and passed to Llama 3, which returns only the information you asked for.

---

## Project Structure

```
├── main.py          # Streamlit UI
├── scrape.py        # Selenium scraper + BeautifulSoup cleaner
├── parse.py         # LangChain + Ollama LLM parser
├── requirements.txt
└── .env             # Optional environment variables
```

---

## Requirements

- Python 3.9+
- Google Chrome installed
- [Ollama](https://ollama.com) installed and running locally with the Llama 3 model pulled

---

## Setup

**1. Clone the repo and install dependencies**

```bash
pip install -r requirements.txt
```

**2. Pull the Llama 3 model via Ollama**

```bash
ollama pull llama3
```

Make sure the Ollama server is running before launching the app:

```bash
ollama serve
```

**3. Run the app**

```bash
streamlit run main.py
```

---

## Usage

1. Paste a full URL into the input field (include `http://` or `https://`).
2. Click **Step 1: Scrape & Clean** — the page loads in a Chrome window, then closes automatically. Cleaned text appears in the expander.
3. Describe what you want to extract, e.g. `List all product prices` or `Find the contact email address`.
4. Click **Step 2: AI Parse** — Llama 3 processes the content and returns only the matching information.

---

## Key Implementation Details

| Component | Detail |
|---|---|
| Browser automation | Selenium with `webdriver-manager` (auto-downloads the correct ChromeDriver) |
| Page wait | 5-second fixed delay after load to allow JS-rendered content to appear |
| HTML parsing | BeautifulSoup with `html.parser`; `<script>` and `<style>` tags removed |
| Chunk size | 6,000 characters per chunk to stay within the LLM context window |
| LLM | `llama3` via `langchain_ollama.OllamaLLM` |
| Prompt | Instructs the model to extract only matching content and return an empty string if nothing matches |

---

## Notes

- To run Chrome without a visible window, uncomment `options.add_argument("--headless")` in `scrape.py`.
- The scraper works best on static or lightly dynamic pages. Heavily JavaScript-dependent SPAs may need a longer wait time.
- Ollama must be running locally — this project does not use any external LLM API.

---

## Dependencies

```
streamlit
langchain
langchain_ollama
selenium
webdriver-manager
beautifulsoup4
lxml
html5lib
python-dotenv
```
