from flask import Flask

app = Flask(__name__)



@app.route('/welcome')
def welcome():
    """Shows the welcome page"""
    return ("welcome")

@app.route('/welcome/home')
def welcome_home():
    """Shows the welcome home page"""
    return ("welcome home")

@app.route('/welcome/back')
def welcome_back():
    """Shows the welcome back page"""
    return ("welcome back")

