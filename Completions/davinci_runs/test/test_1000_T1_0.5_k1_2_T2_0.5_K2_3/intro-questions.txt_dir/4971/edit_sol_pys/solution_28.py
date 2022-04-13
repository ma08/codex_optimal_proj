
#1.py
import sys

def main():
    m = int(sys.stdin.readline().strip())
    x = 1
    while x <= m:
        if len(set([a**3 + b**3 for a in range(1, x) for b in range(1, x)])) >= x:
            return x
        x += 1
    return 'none'

print(main())

#2.py
import sys

def main():
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()
    if n % 2 == 0:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[n // 2]

print(main())

#3.py
import sys

def main():
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        lst.append(sys.stdin.readline().strip())
    m = int(sys.stdin.readline().strip())
    lst2 = []
    for i in range(m):
        lst2.append(sys.stdin.readline().strip())
    for i in lst2:
        if i in lst:
            print('yes')
        else:
            print('no')

main()

#4.py
import sys

def main():
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()
    lst.reverse()
    return sum(lst[::2])

print(main())

#5.py
import sys

def main():
    n = int(sys.stdin.readline().strip())
    lst = []
    for i in range(n):
        lst.append(int(sys.stdin.readline().strip()))
    lst.sort()
    lst.reverse()
    return sum(lst[::2])

print(main())
