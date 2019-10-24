USE spotifydb;
DROP TABLE IF EXISTS Album_Track;
CREATE TABLE Album_Track(
id_album VARCHAR(64) NOT NULL,
id_track VARCHAR(64) NOT NULL,
FOREIGN KEY (id_album) REFERENCES Album(id_album),
FOREIGN KEY (id_track) REFERENCES Track(id_track),
PRIMARY KEY (id_album, id_track)
);