DROP DATABASE IF EXISTS spotifydb;
CREATE DATABASE spotifydb;
USE spotifydb;

DROP TABLE IF EXISTS Usuario;
CREATE TABLE Usuario(
id_user VARCHAR(64) NOT NULL PRIMARY KEY,
display_name VARCHAR(64) NOT NULL,
followers INT NOT NULL
);

DROP TABLE IF EXISTS Playlist;
CREATE TABLE Playlist(
id_playlist VARCHAR(64) NOT NULL PRIMARY KEY,
playlist_name TEXT NOT NULL,
id_user VARCHAR(64) NOT NULL,
collaborative BOOLEAN NOT NULL,
public BOOLEAN NOT NULL,
FOREIGN KEY (id_user) REFERENCES Usuario(id_user)
);

DROP TABLE IF EXISTS Genre;
CREATE TABLE Genre(
genre_name VARCHAR(64) NOT NULL PRIMARY KEY
);

DROP TABLE IF EXISTS Artist;
CREATE TABLE Artist(
id_artist VARCHAR(64) NOT NULL PRIMARY KEY,
artist_name VARCHAR(64) NOT NULL,
followers INT NOT NULL,
popularity INT NOT NULL
);

DROP TABLE IF EXISTS Genre_Artist;
CREATE TABLE Genre_Artist(
id_artist VARCHAR(64) NOT NULL,
genre_name VARCHAR(64) NOT NULL,
FOREIGN KEY (id_artist) REFERENCES Artist(id_artist),
FOREIGN KEY (genre_name) REFERENCES Genre(genre_name),
PRIMARY KEY (id_artist, genre_name)
);

DROP TABLE IF EXISTS Track;
CREATE TABLE Track(
id_track VARCHAR(64) NOT NULL PRIMARY KEY,
track_name VARCHAR(64) NOT NULL,
duration_ms INT NOT NULL,
popularity INT NOT NULL,
explicity BOOLEAN NOT NULL,
danceability DECIMAL(12,6) NOT NULL,
energy DECIMAL(12,6) NOT NULL,
key_note INT NOT NULL,
loudness FLOAT(12,6) NOT NULL,
modee VARCHAR(16) NOT NULL,
speechiness DECIMAL(12,6) NOT NULL,
acousticness DECIMAL(12,6) NOT NULL,
instrumentalness DECIMAL(12,6) NOT NULL,
liveness DECIMAL(12,6) NOT NULL,
valence DECIMAL(12,6) NOT NULL,
tempo DECIMAL(12,6) NOT NULL,
time_signature INT NOT NULL
);

DROP TABLE IF EXISTS Playlist_Track;
CREATE TABLE Playlist_Track(
id_playlist VARCHAR(64) NOT NULL,
id_track VARCHAR(64) NOT NULL,
FOREIGN KEY (id_playlist) REFERENCES Playlist(id_playlist),
FOREIGN KEY (id_track) REFERENCES Track(id_track),
PRIMARY KEY (id_playlist, id_track)
);

DROP TABLE IF EXISTS Artist_Track;
CREATE TABLE Artist_Track(
id_artist VARCHAR(64) NOT NULL,
id_track VARCHAR(64) NOT NULL,
FOREIGN KEY (id_artist) REFERENCES Artist(id_artist),
FOREIGN KEY (id_track) REFERENCES Track(id_track),
PRIMARY KEY (id_artist, id_track)
);

DROP TABLE IF EXISTS Album;
CREATE TABLE Album(
id_album VARCHAR(64) NOT NULL PRIMARY KEY,
album_name VARCHAR(128) NOT NULL,
release_date DATE NOT NULL,
popularity INT NOT NULL,
ntracks INT NOT NULL
);

DROP TABLE IF EXISTS Artist_Album;
CREATE TABLE Artist_Album(
id_artist VARCHAR(64) NOT NULL,
id_album VARCHAR(64) NOT NULL,
FOREIGN KEY (id_artist) REFERENCES Artist(id_artist),
FOREIGN KEY (id_album) REFERENCES Album(id_album),
PRIMARY KEY (id_artist, id_album)
);
