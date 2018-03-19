from flask import Flask, render_template, redirect, request, make_response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import urllib2
import pandas as pd
import json
import urllib2
from pandas.io.json import json_normalize 

import random
import StringIO

def weather_forecast(city):
    url = ('http://api.openweathermap.org/data/2.5/forecast?q=%s&units=imperial&APPID=01a74f4a3f45f9307836e7932ca11a42' % (city))
    res = urllib2.urlopen(url).read()
    weather_json = json.loads(res)

    days_to_forecast = {}
    day_counter = 1
    for i in range(0, 40, 8):
        temp = weather_json['list'][i]['main']['temp']
        #weather = weather_json['list'][1]['weather'][0]['main']
        days_to_forecast.update({day_counter: temp})
        day_counter += 1
    return days_to_forecast
    
app = Flask(__name__)

@app.route('/')
def main():
    return redirect('/index')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/info', methods=['POST', 'GET'])
def info():
    if request.method == 'POST':
        city = request.form['city']
        return render_template('info.html', city=city)
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/plot.png', methods=['POST', 'GET'])
def plot():
    city = request.form['city']
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    temp_list = weather_forecast(city).values()

    axis.plot([1,2,3,4,5], temp_list, 'ro')
    axis.axis([0.5, 5.5, 0, 110])


    canvas = FigureCanvas(fig)
    output = StringIO.StringIO()
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')  

if __name__ == "__main__":
    app.run(debug=True)