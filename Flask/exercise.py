from flask import Flask
import random

app = Flask(__name__)

@app.route('/')
def index():
  return 'Welcome'

@app.route('/create')
def create():
  return 'Create'

@app.route('/read/<id>')
def read(id):
  print(id)
  return 'Read' + id

app.run('0.0.0.0',port=5000,debug=True)