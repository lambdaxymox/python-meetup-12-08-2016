import unittest
import exercises.factorial as fac


class TestFactorial(unittest.TestCase):

	def test_fac_should_reject_non_positive_integers(self):
		"""
		Test that fac only accepts positive integers for input.
		"""
		test_value = -600

		with self.assertRaises(ValueError):
			fac.factorial(test_value)


	def test_fac_should_accept_positive_integers(self):
		test_value = 600

		try:
			result = fac.factorial(test_value)
		except:
			self.fail("Factorial threw an error on a valid input: {}".format(test_value))


	def test_fac_should_reject_non_integer_values(self):
		test_value = 600.1

		with self.assertRaises(ValueError):
			fac.factorial(test_value)