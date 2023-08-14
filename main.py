from ytmusicapi import YTMusic
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import json

client_id = '<Your client id>'
client_secret = '<your client secret>'

SCOPE = 'user-read-private user-read-email user-read-recently-played user-top-read user-read-currently-playing user-library-read user-read-playback-state app-remote-control user-modify-playback-state playlist-read-private playlist-read-collaborative user-follow-read '
REDIRECT_URI = 'http://localhost:8888/callback'


def get_playlists(sp, writeToJson):
    results = sp.current_user_playlists()
    playlists_details = [{'id': playlist['id'], 'name': playlist['name']}
                         for playlist in results['items']]

    if writeToJson:
        with open('playlists.json', 'w') as f:
            json.dump(playlists_details, f, indent=4)

    return playlists_details


def get_playlist_tracks(sp, playlist_id, playlist_name, writeToTxt):
    result = sp.playlist_items(playlist_id)
    playlist_tracks = []

    total_number = result['total']

    for start in range(0, total_number, 100):
        res = sp.playlist_items(playlist_id, offset=start)
        for track in res['items']:
            playlist_tracks.append(track['track']['name'])

    if writeToTxt:
        with open(f'{playlist_name}_tracks.txt', 'w') as f:
            for name in playlist_tracks:
                f.write(name + "\n")

    return playlist_tracks


def make_yt_music_playlist(yt, playlist_name, tracks):
    playlistId = yt.create_playlist(
        playlist_name, 'generated using code written by gokul.')
    added_tracks = []

    unable_to_add = []

    for track in tracks:
        if not track:
            unable_to_add.append(track)
        try:
            search_results = yt.search(track)
            if 'videoId' in search_results[0]:
                added_tracks.append(track)
                yt.add_playlist_items(
                    playlistId, [search_results[0]['videoId']])
                print(f"Added: {track}")
            else:
                unable_to_add.append(track)
        except:
            unable_to_add.append(track)

    return unable_to_add, added_tracks


if __name__ == "__main__":
    sp_oauth = SpotifyOAuth(
        client_id=client_id, client_secret=client_secret, redirect_uri=REDIRECT_URI, scope=SCOPE)
    sp = spotipy.Spotify(auth_manager=sp_oauth)

    yt = YTMusic('oauth.json')

    writeToJson = input(
        "Do you want to write playlist details to a json file?(y/n)")
    playlists = get_playlists(sp, writeToJson == 'y' or writeToJson == 'Y')

    print(f"Found {len(playlists)}. They are:")
    for playlist in playlists:
        print(f"{playlist['id']}    {playlist['name']}")

    if len(playlists) == 0:
        print("No playlists found in spotify. Therefore can't proceed further.")
        exit()

    playlist_id = input(
        "Copy paste the id of the playlist you want to migrate from above: ")

    found = False
    playlist_name = ""

    for playlist in playlists:
        if playlist['id'] == playlist_id:
            found = True
            playlist_name = playlist['name']

    if not found:
        print("Invalid playlist ID entered. Aborting...")
        exit()

    writeToTxt = input(
        "Do you want to write playlist details to a text file?(y/n)")
    playlist_tracks = get_playlist_tracks(
        sp, playlist_id, playlist_name, writeToTxt == 'y' or writeToTxt == 'Y')

    print(f"Found {len(playlist_tracks)} in the playlist {playlist_name}.")

    new_name = input(
        "Enter the name of playlist in youtube music (leave blank for same as spotify): ")
    if new_name == "":
        new_name = playlist_name

    unable_to_add, added = make_yt_music_playlist(
        yt, new_name, playlist_tracks)

    print(
        f"Successfully added {len(added)} songs into the playlist in youtube music - {new_name}")
    print(
        f"Failed to add the following {len(unable_to_add)} songs to the playlist:")
    for t in unable_to_add:
        print(t)
