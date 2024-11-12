import os
import spotipy

import requests
from dotenv import load_dotenv
load_dotenv()




Client_id = os.environ.get("CLIENT_ID")
Client_secret = os.environ.get("CLIENT_SECRET")


# TOEKN_EP_URL = "https://accounts.spotify.com/api/token"

# header = {
#     "Content-Type": "application/x-www-form-urlencoded"
# }
# parameters = {
#     "grant_type" : "client_credentials",
#     "client_id" :  CLIENT_ID,
#     "client_secret" : CLIENT_SECRET
# }
# with requests.post(url=TOEKN_EP_URL,headers=header,data=parameters) as response:
#     response.raise_for_status()
#     print(response.status_code)
#     print(response.text)



#env variables are not working, without env variable everythin is working fine.

