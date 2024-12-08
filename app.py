from flask import Flask, render_template, request
from weather_result import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    else:
        return weather_result(lat_1, lon_1, lat_2, lon_2) #Тут должны быть полученные по запросу корды

if __name__ == '__main__':
    app.run(debug=True)