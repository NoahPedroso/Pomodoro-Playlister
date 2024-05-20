"This is the main script to interact with Spotipy API."
'''Copyright (c) 2024, Noah Pedroso
All rights reserved.

This source code is licensed under the BSD-style license found in the
LICENSE file in the root directory of this source tree. '''

import spotipy
from spotipy.oauth2 import SpotifyOAuth

VERBOSE = True

# Set up authentication

scope = "playlist-modify-private" # Write access to a user's private playlists. (https://developer.spotify.com/documentation/web-api/concepts/scopes#playlist-modify-private)

try:
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))
except spotipy.oauth2.SpotifyOauthError as e:
    print("Failed to authenticate: ", e)
    exit(1)
    # Could also ask for user to input ID and Secret here, seems unsafe though.
if VERBOSE:
    print("Successfully authenticated")

playlists = sp.current_user_playlists()
print(playlists)
while playlists:
    for i, playlist in enumerate(playlists['items']):
        print("%4d. %s %s" % (i + 1 + playlists['offset'], playlist['uri'],  playlist['name']))
    if playlists['next']:
        playlists = sp.next(playlists)
    else:
        playlists = None

# TODO: For some reason it won't find private playlists.  Seems to be a spotify privacy setting issue because they don't show up on my spotify app either.