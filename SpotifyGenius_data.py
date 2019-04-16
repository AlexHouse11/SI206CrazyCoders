import API_Info
import requests 
import json
import spotipy
from spotipy import oauth2

#importing info from API_info.py (Spotify and Genius keys)
spotify_client_ID = API_Info.spotify_client_ID
spotify_client_secret = API_Info.spotify_client_secret
spotify_access_token = API_Info.spotify_access_token
spotify_redirect_URI = API_Info.spotify_redirect_URI

genius_client_ID = API_Info.genius_client_ID
genius_client_secret = API_Info.genius_client_secret
genius_access_token = API_Info.genius_access_token

# Set up authentication to Spotify
sp_auth = oauth2.SpotifyOAuth(spotify_client_ID, spotify_client_secret, spotify_redirect_URI)
sp = spotipy.Spotify(spotify_access_token)

results = sp.current_user()
print(results)




# # Set up your authentication to Genius
# auth = spotipy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)