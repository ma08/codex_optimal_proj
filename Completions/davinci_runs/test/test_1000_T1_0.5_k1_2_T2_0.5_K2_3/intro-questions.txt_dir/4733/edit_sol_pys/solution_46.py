
#https://www.codeeval.com/open_challenges/110/
import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        print(test)
    test_cases.close()

if __name__ == '__main__':
    main()
