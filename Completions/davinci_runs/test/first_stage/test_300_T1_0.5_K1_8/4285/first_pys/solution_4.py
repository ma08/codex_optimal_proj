

import sys

def main():
    n = int(input())
    s = input()
    print(solve(n, s))

def solve(n, s):
    # count the number of a, b and c
    a = 0
    b = 0
    c = 0
    for i in range(n):
        if s[i] == 'a':
            a += 1
        elif s[i] == 'b':
            b += 1
        elif s[i] == 'c':
            c += 1
    
    # count the number of question mark
    q = n - a - b - c
    
    # calculate the number of subsequences 'abc'
    ans = a * b * c
    for i in range(q):
        ans = (ans * 3) % 1000000007
    
    return ans

if __name__ == '__main__':
    sys.exit(main())