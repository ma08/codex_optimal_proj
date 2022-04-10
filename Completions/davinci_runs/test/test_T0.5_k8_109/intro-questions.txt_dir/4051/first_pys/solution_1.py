

from sys import stdin, stdout
from collections import deque

def main():
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    d = deque()
    for i in a:
        d.append(i)

    p = 0
    l = []
    while d:
        i = d.popleft()
        if len(l) > 0 and l[-1] > i + 1:
            p = 1
            break
        l.append(i)
    
    if p == 1:
        stdout.write("NO")
    else:
        stdout.write("YES")

if __name__ == "__main__":
    main()