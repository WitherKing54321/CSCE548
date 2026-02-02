DROP TABLE IF EXISTS anime_genre;
DROP TABLE IF EXISTS anime;
DROP TABLE IF EXISTS genre;
DROP TABLE IF EXISTS studio;

CREATE TABLE studio (
    studio_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL UNIQUE,
    country VARCHAR(60) NOT NULL
);

CREATE TABLE anime (
    anime_id SERIAL PRIMARY KEY,
    title VARCHAR(150) NOT NULL,
    release_year INT NOT NULL CHECK (release_year >= 1960),
    episodes INT NOT NULL CHECK (episodes >= 1),
    studio_id INT NOT NULL,
    CONSTRAINT fk_anime_studio
        FOREIGN KEY (studio_id)
        REFERENCES studio(studio_id)
);

CREATE TABLE genre (
    genre_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE anime_genre (
    anime_id INT NOT NULL,
    genre_id INT NOT NULL,
    PRIMARY KEY (anime_id, genre_id),
    CONSTRAINT fk_anime
        FOREIGN KEY (anime_id)
        REFERENCES anime(anime_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_genre
        FOREIGN KEY (genre_id)
        REFERENCES genre(genre_id)
        ON DELETE CASCADE
);
