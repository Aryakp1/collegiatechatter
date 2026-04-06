from flask import Flask, render_template, request, redirect,  flash, abort
from chatbot import app
from chatbot.models import *
from flask_login import login_user, current_user, logout_user, login_required
from random import randint
import os

import pickle
import json
import random

from flask_session import Session
from flask import session



 




@app.route('/')
def index():
    return render_template("index.html")




@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/courses')
def courses():
    return render_template("courses.html")

@app.route('/events')
def events():
    return render_template("events.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")



with open('chatbot/model/chatbot_model.pkl', 'rb') as f:
    best_model = pickle.load(f)

with open('chatbot/model/vectorizer.pkl', 'rb') as f:
    vectorizer = pickle.load(f)

# Load the intents data 
with open('chatbot/dataset/intents1.json', 'r') as f:
    intents = json.load(f)

def chatbot_response(user_input):
    input_text = vectorizer.transform([user_input])
    predicted_intent = best_model.predict(input_text)[0]
    print(predicted_intent,"---------")
    for intent in intents['intents']:
        if intent['tag'] == predicted_intent:
            response = random.choice(intent['responses'])
            break

    return response

@app.route('/chats')
def home():
    return render_template('chat.html')

@app.route('/chat',methods=['GET','POST'])
def chat():
   
    user_input = request.form['user_input']
    response = chatbot_response(user_input)
    return response





