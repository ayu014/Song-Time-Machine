import os
import spotipy
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()



#----------------------------------------SCRAPING THE SONG DATA--------------------------------------

date = input("Which year do you want to travel to? Enter the date in YYYY-MM-DD format  ")
URL = "https://www.billboard.com/charts/hot-100/" + date
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"
}



response = requests.get(url=URL,headers=header)
print(response.status_code)
contents = response.text

soup = BeautifulSoup(contents,"html.parser")

all_songs = soup.select("li ul li h3")
songs_list =[song.getText().strip() for song in all_songs]
# print(songs_list)



#----------------------------------------------SETUP & AUTHENTICATING THE SPOTIFY WEB API------------------------------


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
    ),
    requests_timeout = 10
)

user_id = sp.current_user()["id"]
# print(user_id)




#-------------------------------------------------------SEARCHING SONG---------------------------------------------
song_urls = []
year = date.split("-")[0]

for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type = "track")
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        # print(uri)
        song_urls.append(uri)
    except IndexError:
        print(f"{song} does not exist on spotify. Skipped!")


#-----------------------------------------------------CREATING THE PLAYLIST----------------------------------------
playlist = sp.user_playlist_create(user=user_id,name=f"{date} Billboard 100",public=False)
playlist_id = playlist["id"]
# print(playlist)

#---------------------------------------------------ADDING SONGS TO THE PLAYLIST---------------------------------------------
sp.playlist_add_items(playlist_id=playlist_id,items=song_urls)


print("Songs added to the playlist.")

    
