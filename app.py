from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('IceBreaker.html')

@app.route('/IceBreaker')
def IceBreaker():
    return render_template('IceBreaker.html')

@app.route('/Engineering')
def Engineering():
    return render_template('Engineering.html')

@app.route('/TruckDepot')
def TruckDepot():
    return render_template('TruckDepot.html')

@app.route('/Weather')
def Weather():
    return render_template('Weather.html')

@app.route('/WeatherStations')
def WeatherStations():
    return render_template('WeatherStations.html')

@app.route('/Privacy')
def Privacy():
    return render_template('Privacy.html')


if __name__ == '__main__':
    app.run(debug=True)