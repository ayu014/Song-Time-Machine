import os
import requests
from bs4 import BeautifulSoup







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
print(songs_list)



    
