from flask import Flask, render_template, redirect, request
import urllib2
import json

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


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html')  

if __name__ == "__main__":
    app.run(debug=True)