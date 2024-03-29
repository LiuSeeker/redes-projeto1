import json
from pprint import pprint
from setup import api_setup, mysql_setup
import time
import datetime
import pymysql

api = api_setup()

conn = mysql_setup()

def str_to_timestamp_parser(texto):
    texto = texto[0:10]
    return time.mktime(datetime.datetime.strptime(texto, "%Y-%m-%d").timetuple())

def genre_insert(genre_list):
    for genre in genre_list:
        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Genre (genre_name) VALUES (%s)", (genre))
            except pymysql.err.IntegrityError as e:
                print("Erro: não foi possivel adicionar o gênero '{}'\n{}\n".format(genre, e))
                pass


def artist_loop(artist_list):
    api = api_setup()
    artists_id = []

    for artist_info in artist_list:
        artist_id = artist_info["id"]
        artists_id.append(artist_id)

        artist = api.artist(artist_id)

        del artist["external_urls"]
        artist["followers"] = artist["followers"]["total"]
        genre_insert(artist["genres"])
        
        #del artist["genres"]
        del artist["href"]
        del artist["images"]
        del artist["type"]
        del artist["uri"]
        name = artist["name"]
        popularity = artist["popularity"]
        followers = artist["followers"]

        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Artist (id_artist, artist_name, popularity, followers) "
                "VALUES (%s, %s, %s, %s)", (artist_id, name, popularity, followers))
            except pymysql.err.IntegrityError as e:
                print("Erro: não foi possivel adicionar o artista '{}'\n{}\n".format(name, e))
        
        for genre in artist["genres"]:
            with conn.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO Genre_Artist (genre_name, id_artist) "
                    "VALUES (%s, %s)", (genre, artist_id))
                except pymysql.err.IntegrityError as e:
                    print("Erro: não foi possivel adicionar o genero do artista\n{}\n".format(e))

        return artists_id


def track_loop(id_track):
    #id_track = "7HB2Waepqi7Ht68ZLKV2C0"

    with conn.cursor() as cursor:
        try:
            cursor.execute("SELECT * FROM Track WHERE id_track = %s",
                            (id_track))
            select_track_id = cursor.fetchone()
            if select_track_id:
                return 0
        except pymysql.err.IntegrityError as e:
            print("Erro: não foi possivel dar SELECT em Track\n{}\n".format(e))
            pass

    track = api.track(id_track)

    album_id = track["album"]["id"]
    track_artists = track["artists"]

    del track["disc_number"]
    del track["artists"]
    del track["album"]
    del track["available_markets"]
    del track["external_ids"]
    del track["external_urls"]
    del track["href"]
    del track["is_local"]
    del track["preview_url"]
    del track["type"]
    del track["uri"]
    del track["track_number"]

    id_track = track["id"]
    track_name = track["name"]
    popularity = track["popularity"]
    explicit = track["explicit"]
    duration_ms = track["duration_ms"]

    track_features = api.audio_features(id_track)[0]

    if track_features["mode"] == 0:
        track_features["mode"] == "minor"
    else:
        track_features["mode"] == "major"
    del track_features["type"]
    del track_features["id"]
    del track_features["uri"]
    del track_features["track_href"]
    del track_features["analysis_url"]
    del track_features["duration_ms"]

    danceability = track_features["danceability"]
    energy = track_features["energy"]
    key_note = track_features["key"]
    loudness = track_features["loudness"]
    mode = track_features["mode"]
    speechiness = track_features["speechiness"]
    acousticness = track_features["acousticness"]
    instrumentalness = track_features["instrumentalness"]
    liveness = track_features["liveness"]
    valence = track_features["valence"]
    tempo = track_features["tempo"]
    time_signature = track_features["time_signature"]


    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Track (id_track, track_name, duration_ms, popularity, explicity, "
                            "danceability, energy, key_note, loudness, modee, speechiness, acousticness, "
                            "instrumentalness, liveness, valence, tempo, time_signature) VALUES (%s, %s, "
                            "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                            (id_track, track_name, duration_ms, popularity, explicit, danceability, \
                            energy, key_note, loudness, mode, speechiness, acousticness, instrumentalness, \
                            liveness, valence, tempo, time_signature))
        except pymysql.err.IntegrityError as e:
            print("Erro: não foi possivel dar adicionar a track '{}'\n{}\n".format(track_name, e))
            pass

    artists_id = artist_loop(track_artists)

    for artist_id in artists_id:
        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Artist_Track (id_artist, id_track) VALUES (%s, %s)",
                                (artist_id, id_track))
            except pymysql.err.IntegrityError as e:
                print("Erro: não foi possivel dar adicionar a track do artista\n{}\n".format(e))
                pass

    album = api.album(album_id)
    del album["album_type"]
    album_artists = album["artists"]
    del album["available_markets"]
    del album["copyrights"]
    del album["external_ids"]
    del album["external_urls"]
    album_genres = album["genres"]
    del album["href"]
    del album["images"]
    album_name = album["name"]
    album_popularity = album["popularity"]
    album_release_date = album["release_date"] #+ " 00:00:01"
    album_release_date = album_release_date.replace("'", "")
    del album["release_date_precision"]
    album_ntracks = album["total_tracks"]
    album_tracks = album["tracks"]["items"]
    del album["type"]
    del album["uri"]

    genre_insert(album_genres)
    

    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Album (id_album, album_name, release_date, popularity, ntracks) "
                            "VALUES (%s, %s, STR_TO_DATE(%s, '%%Y-%%m-%%d'), %s, %s)",
                            (album_id, album_name, album_release_date, album_popularity, album_ntracks))
        except pymysql.err.IntegrityError as e:
            print("Erro: não foi possivel dar adicionar o album '{}'\n{}\n".format(album_name, e))
            pass
    
    album_artists_id = artist_loop(album_artists)

    for album_artist_id in album_artists_id:
        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Artist_Album (id_artist, id_album) VALUES (%s, %s)",
                                (album_artist_id, album_id))
            except pymysql.err.IntegrityError as e:
                print("Erro: não foi possivel dar adicionar o album do artista\n{}\n".format(e))
                pass


    album_tracks = api.album_tracks(album_id)
    for track in album_tracks["items"]:
        track_loop(track["id"])
        
    

def playlist_loop(user_id):
    user_playlists = api.user_playlists(user_id)
    return_tracks = []
    return_playlist_id = []

    for playlist in user_playlists["items"]:
        del playlist["external_urls"]
        del playlist["href"]
        #playlist["images"] = playlist["images"][0]["url"]
        #playlist["image"] = playlist.pop("images")
        playlist["owner"] = playlist["owner"]["id"]
        playlist["owner_id"] = playlist.pop("owner")
        del playlist["primary_color"]
        del playlist["snapshot_id"]
        playlist["playlist_name"] = playlist.pop("name")
        del playlist["type"]
        del playlist["uri"]
        return_tracks.append(playlist["tracks"])
        return_playlist_id.append(playlist["id"])

        with conn.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO Playlist (id_playlist, playlist_name, id_user, collaborative, public) "
                                "VALUES (%s, %s, %s, %s, %s)",
                                (playlist["id"], playlist["playlist_name"], playlist["owner_id"], 
                                playlist["collaborative"], playlist["public"]))
            except pymysql.err.IntegrityError as e:
                print("Erro: não foi possivel dar adicionar a playlist '{}'\n{}\n".format(playlist["playlist_name"], e))
                pass

    return (return_playlist_id, return_tracks)


def user_loop(user_id):
    user = api.user(user_id)

    del user["external_urls"]
    del user["href"]
    user["followers"] = user["followers"]["total"]
    del user["images"]
    del user["type"]
    del user["uri"]

    with conn.cursor() as cursor:
        try:
            cursor.execute("INSERT INTO Usuario (id_user, display_name, followers) VALUES (%s, %s, %s)",
                            (user["id"], user["display_name"], user["followers"]))
        except pymysql.err.IntegrityError as e:
            print("Erro: não foi possivel dar adicionar o usuario '{}'\n{}\n".format(user["display_name"], e))
            pass

    playlist_return = playlist_loop(user_id)

    for i in range(len(playlist_return[0])):
        playlist_tracks = api._get(playlist_return[1][i]["href"])
        for playlist_track in playlist_tracks["items"]:
            track_loop(playlist_track["track"]["id"])
            

            with conn.cursor() as cursor:
                try:
                    cursor.execute("INSERT INTO Playlist_Track (id_playlist, id_track) VALUES (%s, %s)",
                                    (playlist_return[0][i], playlist_track["track"]["id"]))
                except pymysql.err.IntegrityError as e:
                    print("Erro: não foi possivel dar adicionar a track na playlist\n{}\n".format(e))
                    pass

'''
with open("track.json", "w+") as fp:
    json.dump(track, fp, indent=4)
'''


def main():
    print("")
    #with conn.cursor() as cursor:
    #    cursor.execute('START TRANSACTION')
    with conn.cursor() as cursor:
        cursor.execute('SET autocommit=1')
    user_loop("22cibcwsgccqgovymihtk5v7y") #liu
    #user_loop("31rkh7kc52ktphhx6pdnidpcf2he") #joao gindro
    #user_loop("lucasvaz97") #tarraf
    #with conn.cursor() as cursor:
    #    cursor.execute('COMMIT')


if __name__ == '__main__':
    main()