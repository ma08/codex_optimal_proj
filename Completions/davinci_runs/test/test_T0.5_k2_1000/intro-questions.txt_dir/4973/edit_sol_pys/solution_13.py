

#!/usr/bin/env python3

import os
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    count = 0
    for i in range(len(s)):
        if s[i] == 'a':
            count += 1
    count *= n // len(s)
    for i in range(n % len(s)):
        if s[i] == 'a':
            count += 1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')  # os.environ['OUTPUT_PATH']

    s = input()

    n = int(input())  # int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
