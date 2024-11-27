import requests
import time

# API de OpenWeatherMap
url = 'http://172.18.0.2:5000' 


while True:
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("La página está respondiendo correctamente.")
        else:
            print(f"Error: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar: {e}")
    time.sleep(1)