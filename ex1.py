import sys


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
