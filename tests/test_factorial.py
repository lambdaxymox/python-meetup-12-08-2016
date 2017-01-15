import unittest
import exercises.factorial as fac


class TestFactorial(unittest.TestCase):

    def test_fac_should_reject_negative_integers(self):
        """
        Test that fac only accepts positive integers for input.
        """
        test_value = -600

        with self.assertRaises(ValueError):
            fac.factorial(test_value)


    def test_fac_should_accept_positive_integers(self):
        """
        Factorial should accept positive integers.
        """
        test_value = 600

        try:
            fac.factorial(test_value)
        except:
            self.fail("Factorial threw an error on a valid input: {}".format(test_value))


    def test_fac_should_reject_non_integer_values(self):
        """
        Factorial is not defined for non-integer values.
        """
        test_value = 600.1

        with self.assertRaises(ValueError):
            fac.factorial(test_value)


    def test_fac(self):
        """
        Our factorial function should produce correct results.
        """
        fac_table = \
            { 
                0 : 1, 
                1 : 1, 
                2 : 2, 
                3 : 6, 
                4 : 24, 
                5 : 120, 
                6 : 720, 
                7 : 5040,
                8 : 40320, 
                9 : 362880, 
                10 : 3628800
            }

        for i in fac_table.keys():
            result = fac.factorial(i)
            correct_result = fac_table[i]

            self.assertEqual(result, correct_result)
