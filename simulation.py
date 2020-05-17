from flask import Flask, render_template
import json

app = Flask(__name__)

def get_data_from_json():
  input_file = open('data.json')
  return json.load(input_file)

json_array = get_data_from_json()

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

# TODO: Remove this after adding data
@app.route('/posts')
def posts():
  return render_template('posts.html', posts=json_array["posts"])

@app.route('/about')
def about():
  return render_template('about.html')

@app.route('/data')
def data():
  return json_array
