from flask import Flask, render_template
from flask import request, redirect
import json, random

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
@app.route('/somme1', methods=["GET", "POST"])
def sum1():
  return render_template('sum1.html', methods=["GET", "POST"])

@app.route('/somme2')
def sum2():
  return render_template('sum2.html')

@app.route('/factorielle1')
def factorial1():
  return render_template('factorial1.html')

@app.route('/factorielle2')
def factorial2():
  return render_template('factorial2.html')

@app.route('/fibonacci1')
def fibonacci1():
  return render_template('fibonacci1.html')

@app.route('/fibonacci2')
def fibonacci2():
  return render_template('fibonacci2.html')

@app.route('/fibonacci3')
def fibonacci3():
  return render_template('fibonacci3.html')

if __name__ == "__main__":
  app.run()
