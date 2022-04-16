
import sys
import math

def main():
    test_cases = open(sys.argv[1], 'r')
    for test in test_cases:
        test = test.strip().split()
        n = int(test[0])
        s = test[1]
        if n % 2 == 0:
            if s == "out":
                print(math.log(n, 2))
            else:
                print(math.log(n, 2) + 1)
        else:
            if s == "out":
                print(math.log(n, 2) + 1)
            else:
                print(math.log(n, 2))
    test_cases.close()

main()
