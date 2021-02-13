from math import sqrt
from random import uniform

def distance(pos1: (int, int), pos2: (int, int)) -> float:
	return sqrt(
		((pos2[0] - pos1[0])**2) +
		((pos2[1] - pos1[1])**2)
		)

def variance(val1: float, val2: float, variance: float) -> float:

	return ((val1 + val2) / 2) + uniform(-(variance/2), variance/2)