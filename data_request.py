import requests
import json

def get_API_key():
    with open('secrets\\API_key.txt', 'r') as key:
        return key.read()
    
def get_location_key(lat, lon, API_key):
    url = 'http://dataservice.accuweather.com/locations/v1/cities/geoposition/search'
    response = requests.get(f'{url}?apikey={API_key}&q={lat},{lon}')
    if response.status_code == 200:
        data = response.json()
        return data['Key']
    else:
        print('Произошла ошибка при получении ключа города по координатам.\nВозвращен ключ города Москва.\nСохранение информации об ошибки в файле location_key_err.json')
        with open('location_key_err.json', 'w') as err_log:
            err_data = response.json()
            json.dump(err_data, err_log, indent=4)
        return '2515351'

def get_weather_data(lat, lon):
    API_key = get_API_key()
    location_key = get_location_key(lat, lon, API_key)
    url = f'http://dataservice.accuweather.com/forecasts/v1/daily/1day/{location_key}'
    response = requests.get(f'{url}?apikey={API_key}&details=true&metric=true')
    if response.status_code == 200:
        data = response.json()
        data['status'] = 'ok'
        return data
    else:
        print('Произошла ошибка при получении прогноза погоды')
        data = response.json()
        data['status'] = 'err'
        return data

if __name__ == '__main__':
    with open('weather_data.json', 'w') as file:
        data = get_weather_data(55.7558, 37.6173)
        json.dump(data, file, indent=4)
