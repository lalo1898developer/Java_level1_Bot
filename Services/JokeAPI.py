import requests

class JokeAPI():
    def __init__(self):
        self.base_uri = "https://v2.jokeapi.dev/joke/Programming?type=single"

    def get_joke(self):
        res = requests.get(self.base_uri)
        if res.status_code == 200:
            joke = res.json()["joke"]
            return f"😂 {joke}"
        return None