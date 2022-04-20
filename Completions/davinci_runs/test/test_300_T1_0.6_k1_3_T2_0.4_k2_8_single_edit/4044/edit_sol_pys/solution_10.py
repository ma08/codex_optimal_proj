

#Solution

#!/usr/bin/python

if __name__ == '__main__':
    n, m, a = map(int, raw_input().split())
    if (n % a == 0):
        x = n / a
    else:
        x = n / a + 1
    if (m % a == 0):
        y = m / a
    else:
        y = m / a + 1
    print x * y
