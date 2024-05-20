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
