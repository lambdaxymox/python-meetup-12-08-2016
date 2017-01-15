"""
Integration Tests
"""
import unittest
import textwrap
import io
import exercises.parser    as exparser
import exercises.factorial as fac


# The first 20 integers in a string for parsing.
FILE_INPUT = '''\
    20
    1
    2
    3
    4
    5
    6
    7
    8
    9
    10
    11
    12
    13
    14
    15
    16
    17
    18
    19
    20'''

FAC_DICT = {
    1  : 1,
    2  : 2,
    3  : 6,
    4  : 24,
    5  : 120,
    6  : 720,
    7  : 5040,
    8  : 40320,
    9  : 362880,
    10 : 3628800,
    11 : 39916800,
    12 : 479001600,
    13 : 6227020800,
    14 : 87178291200,
    15 : 1307674368000,
    16 : 20922789888000,
    17 : 355687428096000,
    18 : 6402373705728000,
    19 : 121645100408832000,
    20 : 2432902008176640000
}

def file_input():
    return textwrap.dedent(FILE_INPUT.decode('utf_8'))


def mock_file(string):
    return io.StringIO(string)


class TestIntegration(unittest.TestCase):

    def test_ex1_integration(self):
        handle = mock_file(file_input())
        parser = exparser.FileParser()
        values = parser.parse(handle)
        keys   = FAC_DICT.keys()

        for value in values:
            if value not in keys:
                self.fail()

        results = map(lambda n: (n, fac.factorial(n)), values)

        for result in results:
            n, facn = result
            self.assertEqual(facn, FAC_DICT[n])
