

#Solution

#!/bin/python3

if __name__ == '__main__':
    a, b, x = map(int, input().split())
    n = a + b
    s = ''
    for i in range(n):
        if (i < x):
            s += '0'
        else:
            s += '1'
    print(s)
