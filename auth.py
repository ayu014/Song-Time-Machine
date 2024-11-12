import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv

load_dotenv()

Client_id = os.environ.get("CLIENT_ID")
Client_secret = os.environ.get("CLIENT_SECRET")

sp = spotipy.Spotify(
    auth_manager = SpotifyOAuth(
        scope = "playlist-modify-private",
        redirect_uri = "https://example.com",
        client_id = Client_id,
        client_secret = Client_secret,
        show_dialog = True,
        cache_path = "token.txt",
        username = "31tqpcu5bhyl57zmuj675k6awrvi"
    )
)

user_id = sp.current_user()["id"]
print(user_id)