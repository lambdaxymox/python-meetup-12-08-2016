import functools, operator
import sys


def factorial(n):
	if n < 0:
		raise ValueError('Factorial is undefined for negative integer values. Got {}'.format(n))
	else:
	    return functools.reduce(operator.mul, range(2,n+1), 1)


def parse(string):
	lines = string.rstrip().split('\n')
	values = []

	try:
		head, *tail = lines
	except ValueError as e:
		raise e

	try:
		count = int(head, base=10)
	except ValueError as e:
		raise e

	if count != len(tail):
		raise ValueError('Corrupt file. Got {} numbers. Needed {} numbers.'.format(count, len(tail)))

	for line in tail:
		try:
			value = int(line, base=10)
			values.append(value)
		except ValueError as e:
			raise e

	return values

def usage():
	return 'USAGE: python ex1.py FILE_NAME | NUMBER'


def main():
	if len(sys.argv) < 2:
		print(usage())
		sys.exit(1)

	fname = sys.argv[1]

	with open(fname, 'r') as handle:
		string = handle.read()
		result = map(lambda n: (n, factorial(n)), filter(lambda n: n >= 0 and n <= 20, parse(string)))
		
		for res in result:
			n, facn = res
			print('factorial({}) = {}'.format(n, facn))


if __name__ == '__main__':
	main()