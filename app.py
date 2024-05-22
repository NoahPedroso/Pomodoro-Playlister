"This is the main script to interact with Spotipy API."
'''Copyright (c) 2024, Noah Pedroso
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. '''

import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth

VERBOSE = True

### Set up authentication

# For some reason modify private doesn't get a full list? it only can read public playlists published to profile? strange.
# scope = "playlist-modify-private" # Write access to a user's private playlists. (https://developer.spotify.com/documentation/web-api/concepts/scopes#playlist-modify-private)

scope = "playlist-read-private" # Read access to a user's private playlists. (https://developer.spotify.com/documentation/web-api/concepts/scopes#playlist-read-private)

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
except spotipy.oauth2.SpotifyOauthError as e:
    print("Failed to authenticate: ", e)
    exit(1)
    # Could also ask for user to input ID and Secret here, seems unsafe though.
if VERBOSE:
    print("Successfully authenticated")

### Get user's playlists (this should later be expanded to choose from any playlist)
playlists: dict = sp.current_user_playlists()
playlist_uri_name_list: list = []
while playlists:
    for i, playlist in enumerate(playlists['items']):
        playlist_uri_name_list.append((playlist['uri'], playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None
  
### Ask user for playlist to modify
print("Here's all of the matching playlists:")
for i, playlist in enumerate(playlist_uri_name_list):
    print(f"{i+1}. {playlist[1]}")
    
# TODO: Clean this input
input = int(input("Enter the number of the playlist you want to use: "))-1

selected_playlist = playlist_uri_name_list[input]
print("Selected playlist: ", selected_playlist[1])

### Get playlist tracks (and lengths)
pl_id = selected_playlist[0]
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.id,total,items.track.album.name,items.track.duration_ms', # 'album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'is_local', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri'
                                 additional_types=['track'])
    if len(response['items']) == 0:
        break

    pprint(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])
    
### Ask user for Pomodoro Options
pomdodoro_options = {
    "work": 25,
    "short_break": 5,
    "long_break": 15,
    "pomodoro_count": 4,
    "new_playlist": False,
}

### Create Pomodoro Playlist
# TODO

# TODO: abstract into classes (kinda small right now, and also the spotipy api is pretty compartmentalized already)