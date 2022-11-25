import pyrebase
from flask import *
import requests
app = Flask(__name__)


@app.route('/Home')
@app.route('/')

def home():
	return render_template('Home.html')

@app.route('/login')

def basic():
	return render_template('login.html')

@app.route('/about')

def about():
	return render_template('about.html')

@app.route('/register')

def register():
	return render_template('register.html')


@app.route('/ask')

def ask():
	return render_template('ask.html')






if __name__ == '__main__':
	app.run()