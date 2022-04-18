
from collections import defaultdict
import sys

def main():
    # Read input 

    n,k = map(int,sys.stdin.readline().split())
    a = [int(x) for x in sys.stdin.readline().split()]
    d = defaultdict(int)
    for i in a:
        d[i]+=1
    l = list(d.keys())
    l.sort()
    for i in range(len(l)):
        if d[l[i]]>k:
            print(l[i])
            sys.exit()
    print(-1)


if __name__ == '__main__':
    main()
