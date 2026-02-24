import requests

BASE = "http://127.0.0.1:8000"

def show(r):
    print(f"{r.request.method} {r.url} -> {r.status_code}")
    try:
        print(r.json())
    except Exception:
        print(r.text)
    print("-" * 60)
    return r

def must_ok(r):
    if r.status_code >= 400:
        raise SystemExit("Stopping because a request failed.")
    return r

def main():
    # Health
    must_ok(show(requests.get(f"{BASE}/health")))

    # Create studio (returns int)
    r = must_ok(show(requests.post(f"{BASE}/studios", json={"name": "TEST STUDIO", "country": "USA"})))
    studio_id = r.json()

    # Create genre (returns int)
    r = must_ok(show(requests.post(f"{BASE}/genres", json={"name": "TEST GENRE"})))
    genre_id = r.json()

    # Create anime (returns int)
    anime_payload = {
        "title": "TEST ANIME",
        "release_year": 2025,
        "episodes": 12,
        "studio_id": studio_id,
    }
    r = must_ok(show(requests.post(f"{BASE}/anime", json=anime_payload)))
    anime_id = r.json()

    # Read anime
    must_ok(show(requests.get(f"{BASE}/anime/{anime_id}")))

    # Update anime (returns bool)
    update_payload = {
        "title": "TEST ANIME UPDATED",
        "release_year": 2026,
        "episodes": 24,
        "studio_id": studio_id,
    }
    must_ok(show(requests.put(f"{BASE}/anime/{anime_id}", json=update_payload)))

    # Read again
    must_ok(show(requests.get(f"{BASE}/anime/{anime_id}")))

    # Add genre mapping (returns bool)
    must_ok(show(requests.post(f"{BASE}/anime/{anime_id}/genres/{genre_id}")))

    # Remove genre mapping (returns bool)
    must_ok(show(requests.delete(f"{BASE}/anime/{anime_id}/genres/{genre_id}")))

    # Update studio country (returns bool)
    must_ok(show(requests.put(f"{BASE}/studios/{studio_id}/country", json={"country": "JAPAN"})))

    # Cleanup
    must_ok(show(requests.delete(f"{BASE}/anime/{anime_id}")))
    must_ok(show(requests.delete(f"{BASE}/studios/{studio_id}")))

    # Lists at end
    must_ok(show(requests.get(f"{BASE}/anime")))
    must_ok(show(requests.get(f"{BASE}/studios")))
    must_ok(show(requests.get(f"{BASE}/genres")))

if __name__ == "__main__":
    main()