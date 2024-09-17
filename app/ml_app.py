from flask import Flask, render_template
import numpy as np
from markupsafe import escape

import sys
sys.path.append('src/')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules

app = Flask(__name__)

@app.route('/')
@app.route('/<view>')
def home(view = False):
	return render_template('index.html', view = view, tests = get_tests())

def get_tests():
	return ["test1", "test2", "test3", "test4"]

@app.route('/result')
def result():
	return "Hello hello result."

@app.route('/var_test/<test_test>')
def view_var_test(test_test):
	return f'Hello {escape(test_test)}'