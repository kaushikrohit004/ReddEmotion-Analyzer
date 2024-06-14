#!/usr/bin/python3

from flask import Flask, jsonify, request
from flask_cors import CORS
app = Flask(__name__) 
CORS(app)
from reddit_sentiment_analysis import *


incomes = [
    { 'description': 'salary', 'amount': 5000 }
]


@app.route('/')
def get_incomes():
    top, picks_ayz, scores, picks, times = main()
    print("=====================================")
    print(type(top))
    print(picks_ayz)
    return jsonify({"top":top, "scores":scores})


@app.route('/incomes', methods=['POST'])
def add_income():
    incomes.append(request.get_json())
    return '', 204