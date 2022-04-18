
import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        n = int(test.strip())
        if n % 2 == 1:
            print('Alice')
        else:
            print('Bob')
