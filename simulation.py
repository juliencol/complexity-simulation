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

if __name__ == "__main__":
  app.run()
