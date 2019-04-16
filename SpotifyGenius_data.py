import API_Info
import requests 
import json
import spotipy
import oauthlib

#importing info from API_info.py (Spotify and Genius keys)
spotify_client_ID = API_Info.spotify_client_ID
spotify_client_secret = API_Info.spotify_client_secret
genius_client_ID = API_Info.genius_client_ID
genius_access_token = API_Info.spotify_access_token
genius_client_secret = API_Info.genius_client_secret
genius_access_token = API_Info.genius_access_token


# Set up your authentication to Spotify
auth = spotipy.OAuthHandler(spotify_client_ID, spotify_client_secret)

# Set up your authentication to Genius
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)