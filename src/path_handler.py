from enum import Enum
from pathlib import Path


class PathHandler(Enum):
	SRC_ROOT = Path(__file__)

	ML = SRC_ROOT / 'machine_learning'
	ANALYSIS = SRC_ROOT / 'analysis'
	SIM = SRC_ROOT / 'sim'
	

	# ------

	TESTS = SRC_ROOT.parent / 'tests'
	VIZ = SRC_ROOT.parent / 'visualize'
	DATA = SRC_ROOT.parent / 'data'


	def __truediv__(self, other):
		return self / (+other if type(other) is PathHandler else other)

	def __pos__(self):
		return self.value
