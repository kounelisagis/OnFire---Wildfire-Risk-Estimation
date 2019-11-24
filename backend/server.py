import os
from flask import Flask
from flask import request
from flask_cors import CORS
from flask import jsonify
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle

app = Flask(__name__)
CORS(app)


@ app.route("/neamakri", methods = ["POST"])
def hello():
    pickle_in = open("neamakri.pickle", "rb")
    regression = pickle.load(pickle_in)
    
    data = request.get_json()

    average_temp = data['average_temp']
    avg_wind = data['avg_wind']
    max_temp = data['max_temp']
    max_wind = data['max_wind']
    
    return jsonify(regression.predict(np.array([[average_temp, avg_wind, max_temp, max_wind]]))[0])


@ app.route("/parnitha", methods = ["POST"])
def hello1():
    pickle_in = open("vari.pickle", "rb")
    regression = pickle.load(pickle_in)
    
    data = request.get_json()

    average_temp = data['average_temp']
    avg_wind = data['avg_wind']
    max_temp = data['max_temp']
    max_wind = data['max_wind']
    
    return jsonify(regression.predict(np.array([[average_temp, avg_wind, max_temp, max_wind]]))[0])


@ app.route("/spata", methods = ["POST"])
def hello2():
    pickle_in = open("spata.pickle", "rb")
    regression = pickle.load(pickle_in)
    
    data = request.get_json()

    average_temp = data['average_temp']
    avg_wind = data['avg_wind']
    max_temp = data['max_temp']
    max_wind = data['max_wind']
    
    return jsonify(regression.predict(np.array([[average_temp, avg_wind, max_temp, max_wind]]))[0])


@ app.route("/lavrio", methods = ["POST"])
def hello3():
    pickle_in = open("lavrio.pickle", "rb")
    regression = pickle.load(pickle_in)
    
    data = request.get_json()

    average_temp = data['average_temp']
    avg_wind = data['avg_wind']
    max_temp = data['max_temp']
    max_wind = data['max_wind']
    
    return jsonify(regression.predict(np.array([[average_temp, avg_wind, max_temp, max_wind]]))[0])


if __name__ == '__main__':
	app.run()