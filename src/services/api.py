from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from business import bl

app = FastAPI(title="CSCE 548 Project 2 Services")

# ✅ CORS middleware (allows frontend at :5500 to talk to API at :8000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------
# ROOT + HEALTH
# -----------------
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {
        "message": "Anime DB API is running",
        "try": ["/health", "/anime", "/studios", "/genres", "/docs"],
    }


# -----------------
# ANIME
# -----------------
@app.get("/anime")
def api_list_anime():
    try:
        return bl.list_anime_with_studio()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/anime/{anime_id}")
def api_get_anime(anime_id: int):
    try:
        result = bl.get_anime_by_id(anime_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Anime not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/anime")
def api_create_anime(payload: dict):
    try:
        return bl.create_anime(
            title=payload["title"],
            release_year=int(payload["release_year"]),
            episodes=int(payload["episodes"]),
            studio_id=int(payload["studio_id"]),
        )
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/anime/{anime_id}")
def api_update_anime(anime_id: int, payload: dict):
    try:
        return bl.update_anime(
            anime_id=anime_id,
            title=payload["title"],
            release_year=int(payload["release_year"]),
            episodes=int(payload["episodes"]),
            studio_id=int(payload["studio_id"]),
        )
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/anime/{anime_id}")
def api_delete_anime(anime_id: int):
    try:
        return bl.delete_anime(anime_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------
# STUDIOS
# -----------------
@app.get("/studios")
def api_list_studios():
    try:
        return bl.list_studios()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/studios/{studio_id}")
def api_get_studio(studio_id: int):
    try:
        result = bl.get_studio_by_id(studio_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Studio not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/studios")
def api_create_studio(payload: dict):
    try:
        return bl.create_studio(payload["name"], payload["country"])
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/studios/{studio_id}/country")
def api_update_studio_country(studio_id: int, payload: dict):
    try:
        return bl.update_studio_country(studio_id, payload["country"])
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/studios/{studio_id}")
def api_delete_studio(studio_id: int):
    try:
        return bl.delete_studio(studio_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------
# GENRES
# -----------------
@app.get("/genres")
def api_list_genres():
    try:
        return bl.list_genres()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/genres/{genre_id}")
def api_get_genre(genre_id: int):
    try:
        result = bl.get_genre_by_id(genre_id)
        if result is None:
            raise HTTPException(status_code=404, detail="Genre not found")
        return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/genres")
def api_create_genre(payload: dict):
    try:
        return bl.create_genre(payload["name"])
    except KeyError as e:
        raise HTTPException(status_code=400, detail=f"Missing field: {e}")
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# -----------------
# ANIME <-> GENRE MAPPING
# -----------------
@app.get("/anime/{anime_id}/genres")
def api_list_genres_for_anime(anime_id: int):
    try:
        return bl.list_genres_for_anime(anime_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/genres/{genre_id}/anime")
def api_list_anime_for_genre(genre_id: int):
    try:
        return bl.list_anime_for_genre(genre_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/anime/{anime_id}/genres/{genre_id}")
def api_add_genre(anime_id: int, genre_id: int):
    try:
        return bl.add_genre_to_anime(anime_id, genre_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/anime/{anime_id}/genres/{genre_id}")
def api_remove_genre(anime_id: int, genre_id: int):
    try:
        return bl.remove_genre_from_anime(anime_id, genre_id)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))