import requests


def hae_saa(paikkakunta, api_avain):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={api_avain}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        lampotila_kelvin = data["main"]["temp"]
        lampotila_celsius = lampotila_kelvin - 273.15  # Kelvin -> Celsius
        saakuvaus = data["weather"][0]["description"]

        print(f"Sää paikkakunnalla {paikkakunta}: {saakuvaus.capitalize()}")
        print(f"Lämpötila: {lampotila_celsius:.2f} °C")
    except requests.exceptions.RequestException as e:
        print("Virhe haettaessa säätietoja:", e)
    except KeyError:
        print("Virhe: Paikkakuntaa ei löytynyt. Tarkista nimi ja yritä uudelleen.")


def main():
    api_avain = "OMA_API_KEY"
    paikkakunta = input("Anna paikkakunnan nimi: ")
    hae_saa(paikkakunta, api_avain)

if __name__ == "__main__":
    main()
