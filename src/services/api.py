from fastapi import FastAPI, HTTPException
from business import bl

app = FastAPI(title="CSCE 548 Project 2 Services")

# Local run:
#   python3 -m uvicorn services.api:app --reload --port 8000
#
# Hosting notes (fill in later for your chosen platform):
# - Start command: uvicorn services.api:app --host 0.0.0.0 --port $PORT


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/")
def root():
    return {
        "message": "Anime DB API is running",
        "try": ["/health", "/anime", "/studios", "/genres", "/docs"]
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