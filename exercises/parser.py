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