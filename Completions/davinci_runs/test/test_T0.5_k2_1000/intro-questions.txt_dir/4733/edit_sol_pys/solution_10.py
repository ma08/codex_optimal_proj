
# https://www.codeeval.com/open_challenges/136/
import sys

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip()
        if len(test) == 0:
            continue
        test = test.split()
        n = int(test[0])
        shuffle = test[1]
        if shuffle == "out":
            if n % 2 == 0:
                print(n // 2)
            else:
                print((n-1) // 2)
        else:
            if n % 2 == 0:
                print(n // 2)
            else:
                print(n // 2 + 1)
    test_cases.close()

if __name__ == '__main__':
    main()
