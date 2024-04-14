import tidalapi
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os
import base64
import requests
from datetime import datetime


class TDTrack:
    def __init__(self):
        self.AlbumTitle = None
        self.AlbumUPC= None
        self.Artist = None
        self.ISRC = None
        self.tdURL = None

    def set_Artist(self, NamesArr):
        self.Artist = NamesArr

    def set_AlbumTitle(self, Title):
        self.AlbumTitle = Title

    def set_ISRC(self, ISRC):
        self.ISRC = ISRC

    def set_tdURL(self, Url):
        self.tdURL = Url

    def set_UPC(self, UPC):
        self.AlbumUPC = UPC

    def get_UPC(self):
        return self.AlbumUPC

    def get_Artist(self):
        return self.Artist

    def get_AlbumTitle(self):
        return self.AlbumTitle

    def get_Url(self):
        return self.tdURL

    def get_ISRC(self):
        return self.ISRC


class SpTrack:
    def __init__(self):
        self.TrackName=None
        self.AlbumTitle = None
        self.AlbumUPC = None
        self.Artist = None
        self.ISRC = None

    def set_Artist(self, NamesArr):
        self.Artist = NamesArr

    def set_AlbumTitle(self, Title):
        self.AlbumTitle = Title

    def set_ISRC(self, ISRC):
        self.ISRC = ISRC

    def set_UPC(self, UPC):
        self.AlbumUPC = UPC
    def set_TrackTitle(self, Title):
        self.TrackName = Title

    def get_TrackTitle(self):
        return self.TrackName
    def get_UPC(self):
        return self.AlbumUPC

    def get_Artist(self):
        return self.Artist

    def get_AlbumTitle(self):
        return self.AlbumTitle

    def get_ISRC(self):
        return self.ISRC

def get_token():
    client_id = os.getenv('TIDAL_CLIENT_ID')
    client_secret = os.getenv('TIDAL_CLIENT_SECRET')
    if not client_id or not client_secret:
        raise ValueError("TIDAL credentials are missing in environment variables.")
    auth_string = f"{client_id}:{client_secret}"
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = base64.b64encode(auth_bytes).decode("utf-8")
    url = "https://auth.tidal.com/v1/oauth2/token"
    headers = {"Authorization": f"Basic {auth_base64}"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(url, headers=headers, data=data)
    response.raise_for_status()  # Raises HTTPError for bad requests
    token = response.json()["access_token"]
    return token

def load_session(session):
    token_type = os.getenv('TOKEN_TYPE')
    access_token = os.getenv('ACCESS_TOKEN')
    refresh_token = os.getenv('REFRESH_TOKEN')
    timeStr = os.getenv('EXPIRY_TIME')
    expiry_time = datetime.fromisoformat(timeStr)
    session.load_oauth_session(token_type, access_token, refresh_token, expiry_time)

    SpClient = os.getenv('SP_CLIENT_ID')
    SpSecret = os.getenv('SP_CLIENT_SECRET')
    if not (SpClient and SpSecret):
        raise ValueError("Spotify credentials are missing in environment variables.")

    return spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=SpClient,
                                                     client_secret=SpSecret,
                                                     redirect_uri='http://localhost:7777/callback',
                                                     scope='user-library-read playlist-read-private '
                                                           'playlist-read-collaborative'))

if __name__ == '__main__':
    dotenv_path = '../.env'
    load_dotenv(dotenv_path)
    token = get_token()
    session = tidalapi.Session()
    sp = load_session(session)
