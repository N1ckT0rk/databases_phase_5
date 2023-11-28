DROP TABLE IF EXISTS movies;
DROP SEQUENCE IF EXISTS movies_id_seq;

CREATE SEQUENCE IF NOT EXISTS movies_id_seq;
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(255),
    release_year INT
);

INSERT INTO movies
    (title, genre, release_year)
    VALUES('Back to the Future', 'Sci-fi', 1985)