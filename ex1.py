import sys
import exercises.factorial as fac
import exercises.parser    as exparser


def usage():
    return 'USAGE: python ex1.py FILE_NAME | NUMBER'


def main():
    if len(sys.argv) < 2:
        print(usage())
        sys.exit(1)

    fname = sys.argv[1]

    with open(fname, 'r') as handle:
        parser = exparser.FileParser()
        fac_data = parser.parse(handle)
        results = map(lambda n: (n, factorial(n)), fac_data)
        
        for result in results:
            n, facn = result
            print('factorial({}) = {}'.format(n, facn))


if __name__ == '__main__':
    main()
