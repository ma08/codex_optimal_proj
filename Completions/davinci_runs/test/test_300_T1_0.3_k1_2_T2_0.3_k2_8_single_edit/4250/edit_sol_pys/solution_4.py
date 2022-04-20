
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = list(map(int, sys.stdin.readline().split()))  # list of integers
    d = {}
    for i in s:  # count the number of occurrences of each integer
        d[i] = d.get(i, 0) + 1
    t = []
    while len(t) < k:
        m = max(d, key=d.get)
        t.append(m)
        d[m] -= 1
        if d[m] == 0:  # remove the key if the value is 0
            del d[m]
    print(*t)  # print the list

if __name__ == '__main__':
    main()
