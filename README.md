# Mobile Legends Knowledge Graph RAG System

AI-powered Mobile Legends hero information system using Knowledge Graph + RAG (Retrieval-Augmented Generation).

## 🎮 Features

- **Knowledge Graph**: Neo4j database dengan 130+ heroes dan relationships
- **AI-Powered**: Text-to-Cypher + Response Generation models
- **Two Interfaces**:
  - 💻 CLI version (`rag.py`)
  - 🌐 **Web UI** dengan Mobile Legends theme (NEW!)

## 🚀 Quick Start

### Option 1: Web UI (Recommended)

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Configure database:
```bash
# Copy template
copy config_template.toml config.toml

# Edit config.toml dengan Neo4j credentials Anda
```

3. Ingest data (jika belum):
```bash
python ingest_prolog.py
```

4. Start web UI:
```bash
# Automatic (Windows)
start_web_ui.bat

# Manual
# Terminal 1: Backend
python api_server.py

# Terminal 2: Frontend
cd web-ui
npm install
npm run dev
```

5. Open browser: `http://localhost:3000`

📖 **Detailed guide**: See [WEB_UI_GUIDE.md](WEB_UI_GUIDE.md)

### Option 2: CLI Version

```bash
python rag.py
```

## 📁 Project Structure

```
├── api_server.py          # FastAPI backend
├── rag.py                 # CLI interface
├── text_to_cypher.py      # AI: Question → Cypher
├── response_generator.py  # AI: Results → Natural language
├── database.py            # Neo4j driver
├── ingest_prolog.py       # Data ingestion
├── web-ui/                # Next.js frontend
│   ├── app/page.tsx      # Chat interface
│   └── ...
└── prolog_facts/          # Hero data (.pl files)
```

## 🎨 Mobile Legends Theme

Web UI menggunakan official Mobile Legends color palette:
- Primary: Deep Blue (#2B4C7E)
- Accent: Gold (#FDB933)
- Dark: (#0F1419)

## 📖 Documentation

- **Web UI Guide**: [WEB_UI_GUIDE.md](WEB_UI_GUIDE.md)
- **Original Guide**: See below

---

# Original Graph RAG Starter Kit

This repository is prepared for Project Task II, IF4070 Knowledge Representation and Reasoning course (2025-1), STEI-ITB.

## How to use (CLI)
1. (Optional) Make a virtual environment. Command: `py -m venv ./venv`
2. Install required dependencies. Command: `pip install -r requirements.txt`
3. Copy `config_template.toml` to `config.toml`.
4. Modify `config.toml` based on your database configuration.
5. Run RAG system for testing. Command: `py rag.py`
6. Test with one sample question, such as "How many players?".

## Additional configuration
- You may need to change the schema path.
- You may need to set `HF_HOME` environment variable to determine the location of model cache.
  - More information: https://huggingface.co/docs/datasets/cache
- You may need to install other versions of PyTorch to support GPU (and possibly modify the code).
- You may need to change the models for better performance.
- You may need to handle Neo4j exceptions in case the generated Cypher is malformed.

## References
- https://neo4j.com/docs/python-manual/current/
