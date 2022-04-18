

from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    e = int(stdin.readline()) # number of people
    songs = {}
    for i in range(1, n + 1): # initialise songs
        songs[i] = set() # set of people who have heard the song

    for i in range(e):
        line = stdin.readline().split()
        for j in range(1, int(line[0]) + 1): # for each song
            songs[int(line[j])].add(i)

    q = deque()
    q.append(1)
    known = set()
    while len(q) > 0:
        curr = q.popleft()
        known.add(curr)
        for i in range(2, n + 1):
            if i not in known and len(songs[i].difference(songs[curr])) == 0:
                q.append(i)

    for i in range(1, n + 1):
        if i in known:
            print(i)

if __name__ == '__main__':
    main()
