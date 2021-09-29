DROP TABLE IF EXISTS artists;
DROP TABLE IF EXISTS albums;


CREATE TABLE albums (
    id SERIAL PRIMARY KEY,
    album_title VARCHAR(255),
    artists_id INT REFERENCES artists(id)
);


CREATE TABLE artists (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255)

);