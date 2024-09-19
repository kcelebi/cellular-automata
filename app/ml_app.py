from flask import Flask, render_template, Response
from markupsafe import escape
import io


# ------------------

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

# ------------------

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


'''
	Where is this input coming from? Where are we saving data?
	Where are we processing?
'''
@app.route('/plot')
def plot_png():

	# we load the result from the provided drop down or smthn
	xs = range(10)
	ys = [10, 5, -10, 4, 5, 6, 7, 2, 2, 11]
	fig = create_figure(xs, ys)
	output = io.BytesIO()
	FigureCanvas(fig).print_png(output)
	return Response(output.getvalue(), mimetype='image/png')

def create_figure(xs, ys):
	fig = Figure()
	axis = fig.add_subplot(1, 1, 1)
	axis.plot(xs, ys)
	return fig


@app.route('/result')
def result():
	return "Hello hello result."

@app.route('/var_test/<test_test>')
def view_var_test(test_test):
	return f'Hello {escape(test_test)}'