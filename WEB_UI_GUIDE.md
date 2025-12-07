# 🎮 Mobile Legends Knowledge Graph - Web UI

Modern web interface untuk Mobile Legends RAG system dengan tema ML yang keren!

## 📋 Arsitektur

```
┌─────────────────┐      ┌─────────────────┐      ┌─────────────────┐
│   Next.js UI    │ ───> │  FastAPI Server │ ───> │   Neo4j Graph   │
│  (Port 3000)    │      │   (Port 8000)   │      │     Database    │
└─────────────────┘      └─────────────────┘      └─────────────────┘
```

## 🚀 Quick Start

### 1. Install Backend Dependencies

```bash
# Di root directory
pip install fastapi uvicorn pydantic

# Atau update requirements.txt yang sudah ada
pip install -r requirements.txt
```

### 2. Start Backend API Server

```bash
python api_server.py
```

Output yang diharapkan:
```
🚀 Initializing RAG system...
✅ Schema loaded
⏳ Loading Text-to-Cypher model...
✅ Text-to-Cypher ready
⏳ Loading Response Generator model (ini mungkin lama ~3-5 menit)...
✅ Response Generator ready
✅ Database connected
🎉 RAG system ready!
INFO:     Uvicorn running on http://0.0.0.0:8000
```

**PENTING:** Tunggu sampai semua models loaded sebelum start frontend!

### 3. Install Frontend Dependencies

```bash
cd web-ui
npm install
```

### 4. Start Frontend Dev Server

```bash
npm run dev
```

### 5. Open Browser

Buka `http://localhost:3000`

## 🎨 Features

### ✨ UI Features:
- 🎮 **Mobile Legends Theme** - Warna dan style dari ML
- 💬 **Real-time Chat** - Tanya jawab dengan AI
- 📊 **Live Statistics** - Jumlah hero dan relationships
- 📝 **Sample Questions** - Quick access ke pertanyaan umum
- 🔍 **Query Inspector** - Lihat Cypher query yang dihasilkan
- 📱 **Responsive Design** - Works di mobile & desktop
- ⚡ **Fast & Smooth** - Optimized performance

### 🤖 Backend Features:
- 🔥 **FastAPI** - Modern, fast API framework
- 🧠 **AI Models** - Text-to-Cypher + Response Generator
- 💾 **Neo4j Integration** - Direct graph database access
- 🔄 **Fallback System** - Auto-retry dengan backup queries
- 📈 **Statistics API** - Real-time database stats
- ❌ **Error Handling** - Graceful error messages

## 📖 API Documentation

### Endpoints:

#### `GET /`
Health check endpoint
```json
{
  "status": "online",
  "message": "Mobile Legends RAG API"
}
```

#### `POST /chat`
Send question dan terima AI response
```json
// Request
{
  "question": "List all marksman heroes"
}

// Response
{
  "question": "List all marksman heroes",
  "cypher_query": "MATCH (h:Hero)-[:HAS_ROLE]->(r:Role {name: 'marksman'}) RETURN h.name",
  "results": [...],
  "answer": "Here are the marksman heroes: Layla, Miya, ...",
  "success": true
}
```

#### `GET /stats`
Get database statistics
```json
{
  "total_heroes": 130,
  "total_relationships": 450,
  "heroes_by_role": [...]
}
```

## 🎨 Color Palette (Mobile Legends Theme)

| Color | Hex | Usage |
|-------|-----|-------|
| Primary Blue | `#2B4C7E` | Backgrounds, cards |
| Secondary Blue | `#567EBB` | Accents, hover states |
| Gold/Yellow | `#FDB933` | Buttons, highlights |
| Dark BG | `#0F1419` | Main background |
| Light Text | `#E8F1F5` | Text, borders |

## 🛠️ Troubleshooting

### Backend tidak start:
```bash
# Pastikan dependencies installed
pip install fastapi uvicorn pydantic

# Check port 8000 tidak dipakai
netstat -ano | findstr :8000

# Restart
python api_server.py
```

### Frontend error "Failed to connect":
- Pastikan backend running di port 8000
- Check console browser untuk error details
- Pastikan CORS enabled (sudah ada di api_server.py)

### Model loading lama:
- Normal! First time akan download model (~3-6GB)
- Model cached di `~/.cache/huggingface/`
- Subsequent runs akan lebih cepat

### Out of memory:
- Close aplikasi lain
- Butuh minimum 6GB RAM untuk model 3B
- Atau edit `response_generator.py` untuk pakai model lebih kecil

## 📁 File Structure

```
IF4070_mobile-legends-KG-RAG/
├── api_server.py              # FastAPI backend server
├── requirements.txt           # Python dependencies (updated)
├── web-ui/                    # Next.js frontend
│   ├── app/
│   │   ├── page.tsx          # Main chat interface
│   │   ├── layout.tsx        # Layout wrapper
│   │   └── globals.css       # Tailwind + custom styles
│   ├── package.json
│   ├── tailwind.config.js    # ML theme config
│   └── tsconfig.json
├── rag.py                     # CLI version (masih bisa dipakai)
├── database.py
├── text_to_cypher.py
├── response_generator.py
└── ... (other files)
```

## 🎯 Sample Questions

Coba pertanyaan ini di web UI:

1. **List by Role:**
   - "List all marksman heroes"
   - "Show me all tank heroes"
   - "Which heroes are mages?"

2. **Hero Info:**
   - "Who is Layla?"
   - "Tell me about Miya"

3. **Relationships:**
   - "What heroes counter Fanny?"
   - "Show compatible heroes for Angela"

4. **Statistics:**
   - "How many heroes are there?"
   - "Count all heroes"

## 🚀 Production Deployment

### Backend:
```bash
# Install production server
pip install gunicorn

# Run dengan gunicorn
gunicorn api_server:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000
```

### Frontend:
```bash
cd web-ui

# Build production
npm run build

# Start production server
npm start
```

## 📝 Notes

- Backend harus running SEBELUM frontend
- First run akan lama karena download models
- Models di-cache untuk subsequent runs
- Web UI connect ke `http://localhost:8000` by default
- Database credentials dari `config.toml`

## 🎉 Enjoy!

Web UI dengan Mobile Legends theme yang keren sudah siap dipakai! 🎮⚔️
