from data_request import *

def check_temp(forecasts, res_obj):
    min_temp = forecasts['Temperature']['Minimum']['Value']
    max_temp = forecasts['Temperature']['Maximum']['Value']

    if min_temp < 0:
        res_obj['temp_pred'] = 'Будет холодно'
        res_obj['temp'] = min_temp
    elif max_temp > 35:
        res_obj['temp_pred'] = 'Будет жарко'
        res_obj['temp'] = max_temp
    else:
        res_obj['temp_pred'] = 'Обычная температура'
        res_obj['temp'] = [min_temp, max_temp]

def check_wind(forecasts, res_obj):
    wind_speed = forecasts['Day']['Wind']['Speed']['Value']
    if wind_speed > 50:
        res_obj['wind_status'] = 'ok'
        res_obj['wind_pred'] = 'Сильный ветер'
    elif wind_speed < 0:
        res_obj['wind_status'] = 'bad_data'
    else:
        res_obj['wind_status'] = 'ok'
        res_obj['wind_pred'] = 'Ветром не сдует'
    res_obj['wind_speed'] = wind_speed

def check_precipitation(forecasts, res_obj):
    chance = forecasts['Day']['PrecipitationProbability']
    prec_type = forecasts['Day']["PrecipitationType"]

    if chance > 70:
        res_obj['prec_status'] = 'ok'
        res_obj['prec_pred'] = 'Нужно чем-то укрыться'
    elif chance < 0:
        res_obj['prec_status'] = 'bad_data'
    else:
        res_obj['prec_status'] = 'ok'
        res_obj['prec_pred'] = 'Осадков не намечается'
    res_obj['prec_chance'] = chance
    res_obj['prec_type'] = prec_type

def weather_check(weather_data):
    info = {}
    if weather_data['status'] == 'ok':
        check_temp(weather_data['DailyForecasts'][0], info)
        check_wind(weather_data['DailyForecasts'][0], info)
        check_precipitation(weather_data['DailyForecasts'][0], info)
    return info

if __name__ == '__main__':
    with open('weather_data.json', 'r') as file:
        data = json.load(file)
    print(weather_check(data))