import re
import numpy as np


def expect(matrix):
	return

def interpret(literal, x, y=1, z=1):
	def _match(m):
		# print(type(m.group(0)))
		_map = {
			'x' : x,
			'y' : y,
			'z' : z
		}
		return _map[m.group(0)]
	return eval(re.sub(r'[xyz]', _match, literal))

def square_err(t, o):
	return 0.5 * (t - o)**2

def random_gen(n):
	return