-- from the terminal run:
-- psql < music.sql

DROP DATABASE IF EXISTS music;

CREATE DATABASE music;

\c music
CREATE TABLE producers
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO producers
  (name)
VALUES
  ('Dust Brothers'),
  ('Stephen Lironi'),
  ('Roy Thomas Baker'),
  ('Walter Afanasieff'),
  ('Benjamin Rice'),
  ('Rick Parashar'),
  ('Al Shux');

CREATE TABLE albums
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO albums
  (name)
VALUES
  ('Middle of Nowhere'),
  ('A Night at the Opera'),
  ('Daydream'),
  ('A Star Is Born'),
  ('Silver Side Up'),
  ('Prism');


CREATE TABLE artists
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL
);

INSERT INTO artists
  (name)
VALUES
  ('Hanson'),
  ('Queen'),
  ('Mariah Cary'),
  ('Boyz II Men'),
  ('Lady Gaga'),
  ('Bradley Cooper'),
  ('Nickelback'),
  ('Jay Z');

CREATE TABLE songs
(
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  duration_in_seconds INTEGER NOT NULL,
  release_date DATE NOT NULL,
  artists_id INTEGER REFERENCES artists (id),
  album_id INTEGER REFERENCES albums (id),
  producers_id INTEGER REFERENCES producers (id)
);

INSERT INTO songs
  (title, duration_in_seconds, release_date, artists_id, album_id, producers_id)
VALUES
  ('MMMBop', 238, '04-15-1997', 1, 1, 1),
  ('MMMBop', 238, '04-15-1997', 1, 1, 2),
  ('Bohemian Rhapsody', 355, '10-31-1975', 2, 2, 3),
  ('One Sweet Day', 282, '11-14-1995', 3, 3, 4),
  ('One Sweet Day', 282, '11-14-1995', 4, 3, 4),
  ('Shallow', 216, '09-27-2018', 5, 4, 5),
  ('Shallow', 216, '09-27-2018', 6, 4, 5);
  