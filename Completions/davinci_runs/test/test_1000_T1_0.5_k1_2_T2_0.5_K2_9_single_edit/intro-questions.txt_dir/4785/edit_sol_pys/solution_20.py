

import sys

with open(sys.argv[1], 'r') as test_cases:
    for test in test_cases:
        s = test.strip()
        for i in range(len(s)-1):
            if s[i] == 's' and s[i+1] == 's':
                print('hiss')
                break
        else:
            print('no hiss')
