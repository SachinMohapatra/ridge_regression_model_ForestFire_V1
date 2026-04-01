import pickle
from flask import Flask, request, jsonify, render_template
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

application = Flask(__name__)
app = application


##import ridge regressor and Standard scaler pickle

ridge_Model = pickle.load(open("Model/ridge.pkl", 'rb'))
standard_scaler = pickle.load(open("Model/scaler.pkl", 'rb'))

@app.route("/")
def index():
    return render_template('index.html')

if __name__=="__main__":
    app.run(host="0.0.0.0")