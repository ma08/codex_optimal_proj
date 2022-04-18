
from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    e = int(stdin.readline())  # number of songs
    songs = {}
    for i in range(1, n + 1):
        songs[i] = set()  # set of songs that have been heard by person i

    for i in range(e):
        # add the song to the list of songs heard by person j
        line = stdin.readline().split()
        for j in range(1, int(line[0]) + 1):
            songs[int(line[j])].add(i)

    q = deque()
    q.append(1)
    known = set()  # set of people who know the song
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
