

from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    e = int(stdin.readline())
    songs = {}
    for i in range(1, n+1):
        songs[i] = set()

    for i in range(e):
        line = stdin.readline().split()
        for j in range(1, int(line[0])+1):
            songs[int(line[j])].add(i)

    for i in range(1, n+1):
        q = deque()
        q.append(i)
        known = set()
        while len(q) > 0:
            curr = q.popleft()
            known.add(curr)
            for j in range(1, n+1):
                if j not in known and len(songs[j].difference(songs[curr])) == 0:
                    q.append(j)

        for j in range(1, n+1):
            if j in known:
                print(j)
        print()

if __name__ == '__main__':
    main()
