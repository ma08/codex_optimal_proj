

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    l = []
    r = []
    for i in range(n):
        if i == 0:
            l.append(1)
        else:
            if a[i] > a[i-1]:
                l.append(l[i-1] + 1)
            else:
                l.append(1)
        if i == n-1:
            r.append(1)
        else:
            if a[n-i-1] > a[n-i]:
                r.append(r[i-1] + 1)
            else:
                r.append(1)
    r.reverse()
    print(max(l[i]+r[i]-1 for i in range(n)))
    for i in range(n):
        if l[i] > r[i]:
            print("L", end="")
        else:
            print("R", end="")
    print()

if __name__ == '__main__':
    main()