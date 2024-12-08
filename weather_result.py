from data_request import *
from weather_check import *

def weather_result(lat_1, lon_1, lat_2, lon_2):
    data_1 = get_weather_data(lat_1, lon_1)
    data_2 = get_weather_data(lat_2, lon_2)

    checked_data_1 = weather_check(data_1)
    checked_data_2 = weather_check(data_2)

    if checked_data_1['is_bad'] or checked_data_2['is_bad']:
        return 'Плохая погода'
    else:
        return 'Хорошая погода'

if __name__ == '__main__':
    print(weather_result(55.7558, 37.6173, 55.7558, 37.6173))