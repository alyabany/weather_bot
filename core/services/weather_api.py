from config import Weather_API_KEY
import requests
def get_weather_lat_lon(lat: float, lon: float):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={Weather_API_KEY}&units=metric&lang=ar'
    params = {
        'lat': lat,
        'lon': lon,
        'appid': Weather_API_KEY,
        'units': 'metric',
        'lang': 'en'
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        print(data)
        main = data.get('main',{})
        country = data.get('sys',{}).get('country','Unknown')
        main_temp = f"Temp: {main.get('temp')}\nMax Temp: {main.get('temp_max')}\nMin Temp: {main.get('temp_min')}\nHumidity: {main.get('humidity')}\nPressure: {main.get('pressure')}"
        weather = f"Description: {data.get('weather', [{}])[0].get('description', 'No description')}"
        name = data.get('name','Unknown')
        
       
        return f"Country: {country}\nName: {name}\n\n{weather}\n{main_temp}\n"
    except requests.RequestException:
            return {"error": "Failed to retrieve weather data"}