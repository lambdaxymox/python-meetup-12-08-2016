import functools
import operator


def factorial(n):
    if n < 0:
        raise ValueError(
            'Factorial is undefined for negative integer values. Got {}'.format(n)
        )
    
    try:
        return functools.reduce(operator.mul, range(2,n+1), 1)
    except:
        raise ValueError('factorial() only accepts integral values.')
