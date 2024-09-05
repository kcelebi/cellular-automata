import pytest
import numpy as np

import sys
sys.path.append('../src')

from sim.path_handler import PathHandler as PH
import sim.automata as atm
import analysis.stats as stats
from sim.rules import Rules

def test_tautology():
	assert 1 == 1

# ------------------------------ AUTOMATA.PY

def test_in_range_0():
	assert not atm.in_range(-1, 0, (4, 4))

def test_in_range_1():
	assert not atm.in_range(0, -1, (4, 4))

def test_in_range_2():
	assert not atm.in_range(-1, -1, (4, 4))

def test_in_range_3():
	assert not atm.in_range(2, 5, (4, 4))

def test_in_range_4():
	assert not atm.in_range(5, 3, (4, 4))

def test_in_range_5():
	assert atm.in_range(2, 2, (4, 4))

def test_in_range_6():
	assert atm.in_range(2, 3, (4, 4))

# ------------------------------

# check shape correct
def test_get_neighbors_0():
	assert atm.get_neighbors(1, 1, (3, 3)).shape[1] == 2

# check one valid
def test_get_neighbors_1():
	assert atm.get_neighbors(-1, -1, (3, 3)).shape[0] == 1

# check none valid
def test_get_neighbors_2():
	assert atm.get_neighbors(-2, -2, (3, 3)).shape[0] == 0

# check all valid
def test_get_neighbors_3():
	assert atm.get_neighbors(1, 1, (3, 3)).shape[0] == 8

# check center not included
def test_get_neighbors_4():
	assert ~np.all(atm.get_neighbors(1, 1, (3, 3)) == [1, 1])

# ------------------------------

def test_update_0():
	state = [0, 0, 1, 1, 0, 0]
	assert np.all(atm.update(state, rule = Rules.CONWAY) == [0, 0, 0, 0, 0, 0])


def test_update_1():
	state = [
		[0, 1, 1, 1, 0, 0],
		[0, 1, 0, 0, 0, 0]
	]
	upd = atm.update(state, rule = Rules.CONWAY)
	print(upd)
	assert np.all(upd == [[0, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0]])


