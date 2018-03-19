from flask import Flask, render_template, redirect, request, make_response
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import urllib2
import json
import pandas as pd

import random
import StringIO

# Authenticated API
def weather_forecast(city):
    url = ('http://api.openweathermap.org/data/2.5/weather?q=%s&APPID=(01a74f4a3f45f9307836e7932ca11a42)' % (city))
    res = urllib2.urlopen(url).read()
    return json.loads(res)
   
#forecast = weather_forecast('San Jose')

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

@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]

    axis.plot(xs, ys)
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