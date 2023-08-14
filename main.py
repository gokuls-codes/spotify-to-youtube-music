import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import json

from .keys import client_id, client_secret

scope = 'user-read-private user-read-email user-read-recently-played user-top-read user-read-currently-playing user-library-read user-read-playback-state app-remote-control user-modify-playback-state playlist-read-private playlist-read-collaborative user-follow-read ';
redirect_uri = 'http://localhost:8888/callback'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
sp = spotipy.Spotify(auth_manager=sp_oauth)

# playlist_name = input("Enter playlist name: ")
# playlist_id = input("Enter playlist ID: ")

playlist_name = "100%love"
playlist_id = "3k5OAvMm7ksXQdrJFfHhM2"

result = sp.playlist_items(playlist_id)


with open(f"test.json", 'w') as json_file:
    json.dump(result, json_file, indent=4)

playlist_tracks = []

total_number = result['total']

for start in range(0, total_number, 100):
    result = sp.playlist_items(playlist_id, offset=start)
    for track in result['items']:
        # print(track)
        playlist_tracks.append(track['track']['name'])
    
    
print(len(playlist_tracks))
    
with open(f"{playlist_name}.json", 'w') as json_file:
    json.dump(playlist_tracks, json_file, indent=4)
    
with open(f"{playlist_name}.txt", "w") as f:
    for name in playlist_tracks:
        f.write(name + "\n")
