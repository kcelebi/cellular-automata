from flask import Flask
import numpy as np

import sys
sys.path.append('../src/')

from path_handler import PathHandler as PH
import sim.automata as atm
from sim.rules import Rules

app = Flask(__name__)

@app.route('/')
def hello_world():
	return "<p>Hello world</p>"