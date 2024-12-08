from flask import Flask, render_template, request
from weather_result import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        if data_validation(request.form):
            lat_1 = request.form['lat_1']
            lon_1 = request.form['lon_1']
            lat_2 = request.form['lat_2']
            lon_2 = request.form['lon_2']
            return weather_result(lat_1, lon_1, lat_2, lon_2)
        else:
            return 'Полученны неккоректные данные'

def data_validation(values_obj):
    for value in values_obj.values():
        try:
            float(value)
            return True
        except:
            return False

if __name__ == '__main__':
    app.run(debug=True)