CSCE 548 Anime Database Project
Overview

This project implements a three-tier Anime Database application using PostgreSQL, FastAPI, and a web-based frontend. The system allows users to browse, insert, update, and delete anime records through a web interface that communicates with a backend API and a relational database.

The project evolved through multiple stages of development:

Project 1: Database schema creation and console database access

Project 2: Implementation of a layered architecture with business logic and REST API services

Project 3: Development of a browser-based frontend interface

Project 4: Full system integration, testing, and deployment documentation

The final system demonstrates a complete n-tier architecture with a client layer, service layer, business layer, and data layer.

Architecture

The application follows a layered design where each layer has a specific responsibility.

Client (Web Interface) → Service Layer (FastAPI) → Business Layer → Data Layer → PostgreSQL

Client Layer

HTML and JavaScript interface

Sends API requests to the backend service

Service Layer

Implemented with FastAPI

Handles HTTP requests and routes them to the business layer

Business Layer

Implements business logic

Wraps all database operations

Data Layer

Handles database communication using PostgreSQL

Technologies Used

Python 3
FastAPI
Uvicorn
PostgreSQL
HTML
JavaScript

Python libraries used:

fastapi
uvicorn
psycopg2-binary
requests

Project Structure
Project_1
│
├── project3_frontend
│   ├── index.html
│   └── app.js
│
├── sql
│   ├── create_tables.sql
│   └── insert_data.sql
│
├── src
│   ├── main.py
│   ├── db.py
│   ├── client.py
│   ├── openapi.json
│   │
│   ├── business
│   │   └── bl.py
│   │
│   └── services
│       └── api.py
│
├── requirements.txt
└── README.md
Features

The application supports full CRUD functionality.

Users can:

View all anime records

View all studios

View all genres

Search for anime by ID

View genres associated with an anime

View anime associated with a genre

Add new anime records

Update anime records

Delete anime records

All operations are performed through the FastAPI service layer and stored in the PostgreSQL database.

Setup Instructions
1. Clone the Repository
git clone https://github.com/WitherKing54321/CSCE548.git
cd CSCE548/Project_1
2. Install Python Dependencies

Install the required Python libraries.

pip install -r requirements.txt

If dependencies need to be installed manually:

pip install fastapi uvicorn requests psycopg2-binary
3. Database Setup

Ensure PostgreSQL is installed and running.

Open PostgreSQL:

sudo -u postgres psql

Create the project database:

CREATE DATABASE anime_db;

Exit PostgreSQL:

\q
4. Create Database Tables

Run the SQL script to create the required tables.

sudo -u postgres psql anime_db -f sql/create_tables.sql
5. Insert Initial Data

Populate the database with starter records.

sudo -u postgres psql anime_db -f sql/insert_data.sql

These scripts create the anime, studio, genre, and relationship tables with sample data.

Running the Backend Service

Navigate to the backend source directory.

cd src

Start the FastAPI server.

python3 -m uvicorn services.api:app --reload --port 8000

If successful, the server will run at:

http://127.0.0.1:8000

A health endpoint is available for testing:

GET /health
Running the Frontend

Navigate to the frontend directory.

cd ../project3_frontend

Open the web interface:

xdg-open index.html

The webpage provides the user interface for interacting with the anime database.

API Endpoints
Health

GET /health

Anime

GET /anime
GET /anime/{anime_id}
POST /anime
PUT /anime/{anime_id}
DELETE /anime/{anime_id}

Studios

GET /studios
POST /studios
PUT /studios/{studio_id}/country
DELETE /studios/{studio_id}

Genres

GET /genres
POST /genres

Anime-Genre Mapping

POST /anime/{anime_id}/genres/{genre_id}
DELETE /anime/{anime_id}/genres/{genre_id}

Testing

System testing was performed to verify that all layers communicate correctly.

The following operations were tested successfully:

GET requests retrieving anime, studios, and genres
POST requests inserting new anime records
PUT requests updating existing anime records
DELETE requests removing anime records

Database queries were used to verify that the changes were correctly applied.

Screenshots demonstrating these tests are included in the project documentation.

Deployment

For hosted environments, the API can be started with:

uvicorn services.api:app --host 0.0.0.0 --port $PORT

Database connection settings can be configured using environment variables:

DB_NAME
DB_USER
DB_PASSWORD
DB_HOST
DB_PORT

Author

Brandon Wells
