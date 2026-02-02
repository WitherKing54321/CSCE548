import psycopg2
from psycopg2.extras import RealDictCursor

DB_NAME = "anime_db"
DB_USER = "anime_user"
DB_PASSWORD = "anime_pass"
DB_HOST = "localhost"
DB_PORT = 5432


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT,
    )


# ----------------------------
# STUDIO (CRUD)
# ----------------------------
def create_studio(name: str, country: str) -> int:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO studio (name, country)
                VALUES (%s, %s)
                ON CONFLICT (name) DO UPDATE SET country = EXCLUDED.country
                RETURNING studio_id;
                """,
                (name, country),
            )
            return cur.fetchone()[0]
    finally:
        conn.close()


def list_studios():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT studio_id, name, country FROM studio ORDER BY name;")
            return cur.fetchall()
    finally:
        conn.close()


def update_studio_country(studio_id: int, new_country: str) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "UPDATE studio SET country=%s WHERE studio_id=%s;",
                (new_country, studio_id),
            )
            return cur.rowcount == 1
    finally:
        conn.close()


def delete_studio(studio_id: int) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("DELETE FROM studio WHERE studio_id=%s;", (studio_id,))
            return cur.rowcount == 1
    finally:
        conn.close()


# ----------------------------
# ANIME (CRUD)
# ----------------------------
def create_anime(title: str, release_year: int, episodes: int, studio_id: int) -> int:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO anime (title, release_year, episodes, studio_id)
                VALUES (%s, %s, %s, %s)
                RETURNING anime_id;
                """,
                (title, release_year, episodes, studio_id),
            )
            return cur.fetchone()[0]
    finally:
        conn.close()


def list_anime_with_studio():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT a.anime_id, a.title, a.release_year, a.episodes, s.name AS studio
                FROM anime a
                JOIN studio s ON s.studio_id = a.studio_id
                ORDER BY a.title;
                """
            )
            return cur.fetchall()
    finally:
        conn.close()


def get_anime_by_id(anime_id: int):
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(
                """
                SELECT a.anime_id, a.title, a.release_year, a.episodes, a.studio_id, s.name AS studio
                FROM anime a
                JOIN studio s ON s.studio_id = a.studio_id
                WHERE a.anime_id = %s;
                """,
                (anime_id,),
            )
            return cur.fetchone()
    finally:
        conn.close()


def update_anime(anime_id: int, title: str, release_year: int, episodes: int, studio_id: int) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                UPDATE anime
                SET title=%s, release_year=%s, episodes=%s, studio_id=%s
                WHERE anime_id=%s;
                """,
                (title, release_year, episodes, studio_id, anime_id),
            )
            return cur.rowcount == 1
    finally:
        conn.close()


def delete_anime(anime_id: int) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute("DELETE FROM anime WHERE anime_id=%s;", (anime_id,))
            return cur.rowcount == 1
    finally:
        conn.close()


# ----------------------------
# GENRE + MAPPING (CRUD-ish)
# ----------------------------
def create_genre(name: str) -> int:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO genre (name)
                VALUES (%s)
                ON CONFLICT (name) DO UPDATE SET name = EXCLUDED.name
                RETURNING genre_id;
                """,
                (name,),
            )
            return cur.fetchone()[0]
    finally:
        conn.close()


def list_genres():
    conn = get_connection()
    try:
        with conn.cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute("SELECT genre_id, name FROM genre ORDER BY name;")
            return cur.fetchall()
    finally:
        conn.close()


def add_genre_to_anime(anime_id: int, genre_id: int) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO anime_genre (anime_id, genre_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING;
                """,
                (anime_id, genre_id),
            )
            return cur.rowcount == 1
    finally:
        conn.close()


def remove_genre_from_anime(anime_id: int, genre_id: int) -> bool:
    conn = get_connection()
    try:
        with conn, conn.cursor() as cur:
            cur.execute(
                "DELETE FROM anime_genre WHERE anime_id=%s AND genre_id=%s;",
                (anime_id, genre_id),
            )
            return cur.rowcount == 1
    finally:
        conn.close()
