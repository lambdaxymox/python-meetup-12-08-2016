class ParseError:
	def __init__(self, line_number, text, reason):
		self._line_number = line_number
		self._text = text
		self._reason = reason

	@property
	def line_number(self):
		return self._line_number

	@property
	def text(self):
		return self._text

	@property
	def reason(self):
		return self._reason


class Reason:
	def __init__(self, message):
		self._message = message

	@property
	def message(self):
		return self._message


class NumberParser:
	def __init__(self, base=10):
		self.base = base

	def parse(self, line):
		"""
		Parse a number from a line of text, being tolerant of whitespace and newlines.
		"""
		try:
			value = int(line, base=self.base)
		except:
			raise ValueError("Not a valid integer in given base {}: {}.".format(self.base, line))

		return value


class FileParser:
	def __init__(self):
		self.number_parser = NumberParser()

	def parse(self, handle):
		numbers = []		
		lines = enumerate(handle)

		if not lines:
			raise ValueError('Corrupt file.'.format(count, len(tail)))

		line_number, line = lines.next()

		try:
			count = self.number_parser.parse(line)
		except ValueError as e:
			reason = Reason("Not a valid integer in given base {}: {}.".format(self.number_parser.base, line))
				
			raise ParseError(line_number, line, reason)

		for (line_number, line) in lines:
			try:
				next_number = self.number_parser.parse(line)
			except ValueError as e:
				reason = Reason("Not a valid integer in given base {}: {}.".format(self.number_parser.base, line))
				
				raise ParseError(line_number, line, reason)

			numbers.append(next_number)

		if len(numbers) != count:
			raise ValueError('Corrupt file. Got {} numbers. Needed {} numbers.'.format(count, len(tail)))

		return numbers


"""
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
"""