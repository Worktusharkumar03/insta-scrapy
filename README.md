# 🎯 Project: Instagram Video Scraper + Transcriber + Rewriter (AI Agent Orchestration)

## 🧠 Objective:
Build an automated pipeline that:
1. Scrapes **Instagram videos** based on `#hashtags` or `location`.
2. Downloads those videos (publicly accessible ones only).
3. Transcribes each video using Whisper or an equivalent ASR engine.
4. Filters transcripts by topic, language, or keywords (configurable).
5. Rewrites transcripts (summarize, repurpose, correct, etc.) using LLMs.
6. Saves all outputs (metadata, original transcript, rewritten version) into `.docx` or `.pdf` files.
7. Uses **LangChain** (and optionally CrewAI) to structure the agent flow.

---

## ⚙️ Modules Needed (suggested breakdown):
- `scraper.py`: Scrapes Instagram by tag or location.
- `downloader.py`: Downloads videos from scraped URLs.
- `transcriber.py`: Uses Whisper or Deepgram for speech-to-text.
- `filter.py`: Uses keyword/LLM filtering logic.
- `rewriter.py`: Uses LLM to rewrite/refine the transcription.
- `doc_exporter.py`: Saves results into DOCX.
- `agent_orchestrator.py`: Coordinates flow using LangChain agents/tools.
- `config.yaml`: For runtime config (hashtags, locations, keywords, LLM settings).
- `main.py`: Entry point.

---

## 🧩 Tech Stack Preferences:
- 🧠 LangChain (open-source, preferred over CrewAI unless multi-agent logic becomes essential)
- 🤖 LLM: Open-source LLMs (e.g., Llama 3, Mistral, OpenHermes) via Hugging Face Transformers or Ollama
- 🔊 Transcription: Whisper (open-source, local)
- 📄 Document Generation: `python-docx` (for DOCX), `reportlab` or `pypdf` (for PDF)
- 🧼 Optional: Streamlit for UI, SQLite for logs, Docker for deployment

---

## 🧪 Considerations / Questions:
- 🔐 **How to scrape Instagram reliably without login?**
    - Should we use Instaloader, Selenium, or unofficial APIs?
    - Are we working with public profiles and tags only?
- 📹 **How to detect/parse video URLs and media formats?**
- ⏱️ **Do we handle scheduling (e.g., daily scrape jobs)?**
- 🧾 **What kind of filters?**
    - Language detection?
    - Content classification?
    - Topic relevance?
- ✍️ **Rewrite Goals:**
    - Summary, social caption, or blog-style rewrite?
    - Retain tone or make it SEO-friendly?
- 📄 **Doc Formatting:**
    - Should docx contain thumbnails?
    - Export format: `.docx`, `.md`, `.pdf`?
- ⚙️ Should we Dockerize this for deployment?

---

## 🚀 Next Steps (initial TODO):
- [ ] Set up virtual environment + dependencies
- [ ] Create `config.yaml` with placeholder settings
- [ ] Build `scraper.py` to get post metadata by hashtag
- [ ] Build `downloader.py` to fetch and store video
- [ ] Integrate Whisper to transcribe
- [ ] Build LangChain tools/agents
- [ ] Save output using `python-docx`
- [ ] Add command-line args / config loader

---

## 🧠 Example Command Line Usage:
```bash
python main.py --hashtag nature --location "New York" --keywords wildlife,forest --rewrite_mode "summarize"
```
