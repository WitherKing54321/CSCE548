import db

# -----------------
# STUDIO
# -----------------
def create_studio(name: str, country: str) -> int:
    if not name or not name.strip():
        raise ValueError("name is required")
    if not country or not country.strip():
        raise ValueError("country is required")
    return db.create_studio(name.strip(), country.strip())

def list_studios():
    return db.list_studios()

def update_studio_country(studio_id: int, new_country: str) -> bool:
    if studio_id <= 0:
        raise ValueError("studio_id must be positive")
    if not new_country or not new_country.strip():
        raise ValueError("new_country is required")
    return db.update_studio_country(studio_id, new_country.strip())

def delete_studio(studio_id: int) -> bool:
    if studio_id <= 0:
        raise ValueError("studio_id must be positive")
    return db.delete_studio(studio_id)

# -----------------
# ANIME
# -----------------
def create_anime(title: str, release_year: int, episodes: int, studio_id: int) -> int:
    if not title or not title.strip():
        raise ValueError("title is required")
    if studio_id <= 0:
        raise ValueError("studio_id must be positive")
    if release_year <= 0:
        raise ValueError("release_year must be positive")
    if episodes <= 0:
        raise ValueError("episodes must be positive")
    return db.create_anime(title.strip(), release_year, episodes, studio_id)

def list_anime_with_studio():
    return db.list_anime_with_studio()

def get_anime_by_id(anime_id: int):
    if anime_id <= 0:
        raise ValueError("anime_id must be positive")
    return db.get_anime_by_id(anime_id)

def update_anime(anime_id: int, title: str, release_year: int, episodes: int, studio_id: int) -> bool:
    if anime_id <= 0:
        raise ValueError("anime_id must be positive")
    if not title or not title.strip():
        raise ValueError("title is required")
    if studio_id <= 0:
        raise ValueError("studio_id must be positive")
    if release_year <= 0:
        raise ValueError("release_year must be positive")
    if episodes <= 0:
        raise ValueError("episodes must be positive")
    return db.update_anime(anime_id, title.strip(), release_year, episodes, studio_id)

def delete_anime(anime_id: int) -> bool:
    if anime_id <= 0:
        raise ValueError("anime_id must be positive")
    return db.delete_anime(anime_id)

# -----------------
# GENRE
# -----------------
def create_genre(name: str) -> int:
    if not name or not name.strip():
        raise ValueError("name is required")
    return db.create_genre(name.strip())

def list_genres():
    return db.list_genres()

def add_genre_to_anime(anime_id: int, genre_id: int) -> bool:
    if anime_id <= 0 or genre_id <= 0:
        raise ValueError("IDs must be positive")
    return db.add_genre_to_anime(anime_id, genre_id)

def remove_genre_from_anime(anime_id: int, genre_id: int) -> bool:
    if anime_id <= 0 or genre_id <= 0:
        raise ValueError("IDs must be positive")
    return db.remove_genre_from_anime(anime_id, genre_id)