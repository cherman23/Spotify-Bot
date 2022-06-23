import requests
from requests.auth import HTTPBasicAuth

CLIENT_ID="018eabe29a6b4e02bf97db6152da27b8"
CLIENT_SECRET="a39175b2f95740289cf696b5408e82a4"
TOKEN=""

print("Welcome")

def login():
        global TOKEN
        url = "https://accounts.spotify.com/api/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        form = {
           "grant_type":"client_credentials"
        }
        res = requests.post(url, headers= headers, auth=HTTPBasicAuth(CLIENT_ID, CLIENT_SECRET), data=form)
        if(res.status_code == 200):
                ## save token
                ## redirect to artists search bar
                TOKEN = res.json()
                return TOKEN
        else:
                return res.status_code

def search():
    login()
    artist = input("Enter arist name: ")
    url ="https://api.spotify.com/v1/search"
    payload= {
            "q": artist,
            "type": "artist",
            "limit": 3
    }
    headers = {
            "Content-Type": "application/json", 
            "Authorization": "Bearer " + TOKEN["access_token"]
    }
    res = requests.get(url, headers= headers, params=payload)
    if(res.status_code == 200):
            return res.json()
    else:
            return res.status_code
    ## some button here to get artist name
    ## query spotify for artists
    ## present the top 3 to user
    ## user selects artist

search()

