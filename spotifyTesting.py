'This is the main script to interact with Spotipy API. It is currently just testing.'
'''Copyright (c) 2024, Noah Pedroso
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. '''
import spotipy
from spotipy.oauth2 import SpotifyOAuth

VERBOSE = True
# Set up authentication
scope = 'user-library-read'
# scope = "playlist-modify-public" 
# TODO: Handle spotipy.oauth2.SpotifyOauthError exception here
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
if VERBOSE:
    print("Successfully authenticated")

results = sp.current_user_saved_tracks()
for idx, item in enumerate(results['items']):
    track = item['track']
    print(idx, track['artists'][0]['name'], " – ", track['name'])
