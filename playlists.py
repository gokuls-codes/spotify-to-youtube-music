import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

import json

from .keys import client_id, client_secret

scope = 'user-read-private user-read-email user-read-recently-played user-top-read user-read-currently-playing user-library-read user-read-playback-state app-remote-control user-modify-playback-state playlist-read-private playlist-read-collaborative user-follow-read ';
redirect_uri = 'http://localhost:8888/callback'

sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri, scope=scope)
# auth_manager = SpotifyClientCredentials()

# username = request.user.username
# token = util.prompt_for_user_token(username, show_dialog=True, scope=scope)
sp = spotipy.Spotify(auth_manager=sp_oauth)

# results = sp.current_user_recently_played()

# for res in results['items']:
#     print(res['track']['name'])

results = sp.current_user_playlists()

playlists = []

for playlist in results['items']:
    playlists.append({
        'id': playlist['id'],
        'name': playlist['name'],
    })
    

with open("playlists.json", 'w') as json_file:
    json.dump(playlists, json_file, indent=4) 
