

from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    e = int(stdin.readline())
    songs = [set() for i in range(n+1)]

    for i in range(e):
        line = stdin.readline().split()
        for j in range(1, len(line)):
            songs[int(line[j])].add(line[0])

    q = deque()
    q.append("1")
    known = set()
    while len(q) > 0:
        curr = q.popleft()
        known.add(curr)
        for i in range(1, n+1):
            if str(i) not in known and len(songs[i].difference(songs[int(curr)])) == 0:
                q.append(i)

    for i in range(1, n+1):
        if str(i) in known:
            print(i)

if __name__ == '__main__':
    main()
