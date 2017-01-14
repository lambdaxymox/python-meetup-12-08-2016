import functools, operator
import sys


def factorial(n):
	if n < 0:
		raise ValueError('Factorial is undefined for negative integer values. Got {}'.format(n))
	else:
	    return functools.reduce(operator.mul, range(2,n+1), 1)
