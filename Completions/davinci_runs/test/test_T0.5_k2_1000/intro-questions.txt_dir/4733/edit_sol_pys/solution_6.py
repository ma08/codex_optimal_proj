# https://www.codeeval.com/open_challenges/8/
import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print(test)
    test_cases.close()

main()
