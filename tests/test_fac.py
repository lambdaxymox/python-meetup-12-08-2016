import unittest
import exercises.fac as fac


class TestFactorial(unittest.TestCase):

	def test_fac_should_reject_non_positive_integers(self):
		"""
		Test that fac only accepts positive integers for input.
		"""
		test_value = -600

		with self.assertRaises(ValueError):
			fac.fac(test_value
				)