# CSCE 548 - Project 1 (Anime Database)

This project creates a small relational database (anime/studios/genres) with test data,
plus a console application that retrieves records from the database.

## Folder structure
- `sql/` - SQL scripts to create tables and insert test data
- `src/` - Console app + data access layer code
- `screenshots/` - Proof screenshots for submission

## How to run (will fill in as project progresses)
1. Run `sql/create_tables.sql`
2. Run `sql/insert_data.sql`
3. Run the console app in `src/`

# CSCE 548 – Project 2  
Brandon Wells  

## Overview

This project implements a PostgreSQL-backed Anime Database using a layered architecture:

- Data Access Layer (`db.py`)
- Business Layer (`business/bl.py`)
- Service Layer (FastAPI – `services/api.py`)
- Console Client (`client.py`)

Project 2 extends Project 1 by wrapping all database operations in a Business Layer and exposing them through RESTful microservices.

---

## Architecture

Console Client → Service Layer (FastAPI) → Business Layer → Data Layer → PostgreSQL

All CRUD methods in `db.py` are:
- Wrapped in `business/bl.py`
- Exposed via `services/api.py`
- Tested through `client.py`

---

## Setup

### 1. Install Dependencies

From project root:

```bash
python3 -m pip install -r requirements.txt
```

If needed:

```bash
python3 -m pip install fastapi uvicorn requests psycopg2-binary
python3 -m pip freeze > requirements.txt
```

---

### 2. Database Setup

Ensure PostgreSQL is running.

Run:

```bash
sudo -u postgres psql anime_db -f sql/create_tables.sql
sudo -u postgres psql anime_db -f sql/insert_data.sql
```

Default connection settings:

```
DB_NAME=anime_db
DB_USER=anime_user
DB_PASSWORD=anime_pass
DB_HOST=localhost
DB_PORT=5432
```

Environment variables can override these values for hosting.

---

## Run the Microservice

From `src` directory:

```bash
cd src
python3 -m uvicorn services.api:app --reload --port 8000
```

Test health endpoint:

```bash
python3 -c "import requests; print(requests.get('http://127.0.0.1:8000/health').json())"
```

---

## Run the Console Client (Full CRUD Demo)

In a second terminal:

```bash
cd src
python3 client.py
```

The client demonstrates:

- Create Studio
- Create Genre
- Create Anime
- Read Anime
- Update Anime
- Add/Remove Genre Mapping
- Update Studio Country
- Delete Anime
- Delete Studio
- List remaining records

All operations occur through the service layer (not directly to the database).

---

## API Endpoints

### Health
- GET /health

### Anime
- GET /anime
- GET /anime/{anime_id}
- POST /anime
- PUT /anime/{anime_id}
- DELETE /anime/{anime_id}

### Studios
- GET /studios
- POST /studios
- PUT /studios/{studio_id}/country
- DELETE /studios/{studio_id}

### Genres
- GET /genres
- POST /genres

### Anime-Genre Mapping
- POST /anime/{anime_id}/genres/{genre_id}
- DELETE /anime/{anime_id}/genres/{genre_id}

---

## Hosting

Start command for deployment:

```bash
uvicorn services.api:app --host 0.0.0.0 --port $PORT
```

Environment variables required for hosted database:

```
DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT
```

---

## Status

- Business Layer implemented
- All CRUD methods exposed via microservice
- Console client validates end-to-end functionality
- Ready for hosting