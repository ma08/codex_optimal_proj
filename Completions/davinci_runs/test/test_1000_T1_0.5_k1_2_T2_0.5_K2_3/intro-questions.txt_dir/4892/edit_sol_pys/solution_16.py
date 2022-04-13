
from collections import deque

from sys import stdin

def main():
    n,k = [int(x) for x in stdin.readline().strip().split()]
    d = deque()
    for i in range(n):
        d.append(i+1)
    index = 0
    res = []
    while len(d)>0:
        index += k-1
        index %= len(d)
        res.append(d[index])
        d.remove(d[index])
    print('<'+', '.join([str(x) for x in res])+'>')


if __name__ == '__main__':
    main()
