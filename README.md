# 🎵 Musify

A personal AI-powered music library manager built from scratch as a learning project. Started in Semester 2 with basic Python knowledge — being built up progressively as programming skills grow.

---

## 🚀 Project Vision

Musify is a long-term project evolving from a simple CLI music manager into a full-stack AI-powered music recommendation app — similar to Spotify. The AI engine learns from listening history and imported playlists to recommend songs that match the user's taste.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.14 |
| Backend Framework | FastAPI |
| Database | PostgreSQL |
| DB Connector | psycopg2 |
| Data Validation | Pydantic |
| Environment Variables | python-dotenv |
| Version Control | Git + GitHub |

---

## 📁 Project Structure

```
musify/
├── song.py              # Song class with to_dict and from_dict
├── Playlist.py          # Playlist class with song management
├── User.py              # User class
├── storage.py           # JSON-based storage (Phase 1, legacy)
├── db_storage.py        # PostgreSQL database functions
├── db.py                # Database connection setup
├── api.py               # FastAPI REST API endpoints
├── Main.py              # CLI menu interface
├── data/
│   ├── library.json     # Legacy JSON song storage
│   └── playlists.json   # Legacy JSON playlist storage
├── .env                 # Environment variables (not tracked by git)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

---

## 🗄️ Database Schema

```sql
-- Songs catalog
CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    artist VARCHAR(255) NOT NULL,
    duration INTEGER,
    playcount INTEGER DEFAULT 0
);

-- Playlists
CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Junction table linking songs to playlists (many-to-many)
CREATE TABLE playlist_songs (
    playlist_id INTEGER REFERENCES playlists(id),
    song_id INTEGER REFERENCES songs(id)
);
```

---

## 🌐 REST API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | API status and version |
| GET | `/songs` | Get all songs in library |
| POST | `/songs` | Add a new song to library |
| GET | `/playlists` | Get all playlists |
| POST | `/playlists` | Create a new playlist |
| POST | `/playlists/{id}/songs` | Add a song to a specific playlist |

### Running the API

```bash
python -m uvicorn api:app --reload
```

Visit `http://127.0.0.1:8000/docs` for the interactive Swagger UI.

---

## 💻 CLI Interface

A command-line menu for managing the music library locally:

```
Welcome to Musify!
1) Add song to library
2) Create a playlist
3) Add song to playlist
4) Display playlist
5) Display library
6) Exit
```

### Running the CLI

```bash
python Main.py
```

---

## ⚙️ Setup

### Prerequisites
- Python 3.11+
- PostgreSQL 18

### Installation

```bash
# Clone the repo
git clone https://github.com/Codecrafter1007/Musify.git
cd Musify

# Install dependencies
pip install fastapi uvicorn psycopg2-binary python-dotenv pydantic

# Create .env file
echo "DB_PASSWORD=your_postgres_password" > .env
```

### Database Setup

Run these SQL commands in pgAdmin or psql:

```sql
CREATE DATABASE musify;

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) UNIQUE NOT NULL,
    artist VARCHAR(255) NOT NULL,
    duration INTEGER,
    playcount INTEGER DEFAULT 0
);

CREATE TABLE playlists (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE playlist_songs (
    playlist_id INTEGER REFERENCES playlists(id),
    song_id INTEGER REFERENCES songs(id)
);
```

---

## 🗺️ Development Roadmap

### ✅ Phase 1 — Foundation (Complete)
- Song, Playlist, User classes in C++ and Python
- CLI music manager with 6 menu options
- JSON file persistence
- Multi-file project structure
- Git version control

### ✅ Phase 2 — Web & Database (In Progress)
- [x] PostgreSQL database with relational schema
- [x] Python-PostgreSQL connection via psycopg2
- [x] Full database storage layer replacing JSON
- [x] FastAPI REST API with 6 endpoints
- [x] Pydantic data validation
- [x] Environment variable security
- [ ] React frontend

### 🔲 Phase 3 — AI Engine (Upcoming)
- Song audio feature vectors (energy, danceability, tempo, etc.)
- User taste profile built from listen history
- Cosine similarity recommendation engine
- Spotify API integration for real song data
- Playlist import and AI learning

### 🔲 Phase 4 — Advanced ML (Future)
- Matrix factorization model
- Neural collaborative filtering
- Session-based real-time recommendations

### 🔲 Phase 5 — Polish & Deploy (Future)
- Docker containerization
- Cloud deployment
- Production-ready React UI

---

## 👨‍💻 About This Project

This is a personal learning project started in Semester 2 of college. The goal is to grow the codebase progressively as programming knowledge increases — from a simple CLI tool today to a full AI-powered music app. Every feature is built from scratch to maximise learning.

**Skills being developed:** Python, C++, OOP, SQL, REST APIs, FastAPI, PostgreSQL, Git, and eventually ML/AI with NumPy, scikit-learn and PyTorch.
