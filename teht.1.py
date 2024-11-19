import requests

def hae_chuck_norris_vitsi():
    url = "https://api.chucknorris.io/jokes/random"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        print("Chuck Norris -vitsi:")
        print(data["value"])
    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa vitsiä:", e)


hae_chuck_norris_vitsi()
