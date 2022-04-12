
# SOLUTION
#!/usr/bin/env python
from sys import stdin, stdout
def main():
    t = int(stdin.readline())
    for i in range(t):
        n = int(stdin.readline())
        if n == 2:
            print('YES')
            print('1 2')
        elif n == 4:
            print('YES')
            print('2 4 1 3')
        else:
            print('YES')
            print(*(list(range(2, n, 2)) + list(range(1, n, 2))))
main()
