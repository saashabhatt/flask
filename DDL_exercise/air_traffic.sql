-- from the terminal run:
-- psql < air_traffic.sql

DROP DATABASE IF EXISTS air_traffic;

CREATE DATABASE air_traffic;

\c air_traffic

CREATE TABLE destinations
(
  id SERIAL PRIMARY KEY,
  city TEXT NOT NULL,
  country TEXT NOT NULL
);

INSERT INTO destinations
  (city, country)
VALUES
  ('Washington DC', 'United States'),
  ('Seattle', 'United States'),
  ('Mexico City', 'United States'),
  ('New York', 'United States'),
  ('Charlotte', 'United States'),
  ('Los Angeles', 'United States'),
  ('Sao Paolo', 'Brazil'),
  ('Mumbai', 'India'),
  ('Bengaluru', 'India');

CREATE TABLE airlines
(
  id SERIAL PRIMARY KEY,
  name_ TEXT NOT NULL
);

INSERT INTO airlines
  (name_)
VALUES
  ('British Airways'),
  ('United'),
  ('Delta'),
  ('American Airlines'),
  ('Avianca Brasil'),
  ('Air Canada'),
  ('Air India');

CREATE TABLE flights
(
  id SERIAL PRIMARY KEY,
  departure TIMESTAMP NOT NULL,
  arrival TIMESTAMP NOT NULL,
  airline_id INTEGER REFERENCES airlines (id),
  from_id INTEGER REFERENCES destinations (id),
  to_id INTEGER REFERENCES destinations (id)
);

INSERT INTO flights
  (departure, arrival, airline_id, from_id, to_id)
VALUES
  ('2018-04-08 09:00:00', '2018-04-08 12:00:00', 1, 1, 4),
  ('2018-04-08 09:00:00', '2018-04-08 12:00:00', 2, 4, 3),
  ('2018-04-08 09:00:00', '2018-04-08 12:00:00', 3, 4, 2),
  ('2018-04-08 09:00:00', '2018-04-08 12:00:00', 4, 5, 1),
  ('2018-04-08 09:00:00', '2018-04-08 12:00:00', 5, 6, 2);

CREATE TABLE tickets
(
  id SERIAL PRIMARY KEY,
  first_name TEXT NOT NULL,
  last_name TEXT NOT NULL,
  seat TEXT NOT NULL,
  flight_id INTEGER REFERENCES flights (id)
);

INSERT INTO tickets
  (first_name, last_name, seat, flight_id)
VALUES
  ('Jennifer', 'Finch', '33B', 2),
  ('Thadeus', 'Gathercoal', '8A', 2),
  ('Sonja', 'Pauley', '12F', 3),
  ('Alvin', 'Leathes', '1A', 4),
  ('Berkie', 'Wycliff', '32B', 5),
  ('Cory', 'Squibbes', '10D', 4),
  ('Thadeus', 'Gathercoal', '18C', 2);
