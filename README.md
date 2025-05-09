# 🧠 GenAI Wealth Strategy Assistant

An open-source, offline wealth advisory tool built using:
- 🦙 LLaMA3 (via Ollama)
- 🔎 RAG (LangChain + ChromaDB)
- 💬 Custom guardrails for ethical safety
- 📈 Evaluation metrics
- 🌐 Streamlit UI

## 🚀 Features
- Ingests both local and online financial PDFs
- Safe, tailored portfolio recommendations
- Runs 100% offline (no API key or cloud required)
- Fully containerized with Docker

## 🛠️ Setup

### Local

```bash
pip install -r requirements.txt
ollama run llama3
streamlit run app.py
```

### Docker

```bash
docker build -t wealth-advisor .
docker run -p 8501:8501 wealth-advisor
```

## ✅ Example Use Case

> “What’s the best portfolio strategy for a 35-year-old investor saving for their child’s education with moderate risk appetite?”

## 📂 File Structure

- `app.py` - Streamlit frontend
- `advisor.py` - Core logic with RAG
- `guardrails.py` - Filters unsafe advice
- `metrics.py` - Evaluation placeholder

## 📜 License

MIT License.