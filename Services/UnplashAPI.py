import requests
import os

class UnplashAPI():
    def __init__(self):
        self.access_key = os.getenv('ACCESSKEY_UNPLASH')
        self.base_uri = "https://api.unsplash.com/photos/random"

    def get_image(self):
        uri = self.base_uri + '?query=programming&client_id=' + self.access_key
        res = requests.get(uri)
        if res.status_code == 200:
            image = res.json()["urls"]["regular"]
            return f"[😎]({image})"
        return None