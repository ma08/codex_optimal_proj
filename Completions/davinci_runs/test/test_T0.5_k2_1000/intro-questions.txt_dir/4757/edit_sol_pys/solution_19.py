
from sys import stdin
from collections import deque

def main():
    n = int(stdin.readline())
    e = int(stdin.readline()) # number of songs
    songs = {}
    for i in range(1, n+1):
        songs[i] = set() # set of songs that person i knows

    for i in range(e):
        line = stdin.readline().split()
        for j in range(1, int(line[0])+1): # add song i to all people who know it
            songs[int(line[j])].add(i)

    q = deque() # queue for bfs
    q.append(1)
    known = set() # set of people who know all songs
    while len(q) > 0:
        curr = q.popleft()
        known.add(curr)
        for i in range(2, n+1): # check all people who haven't been checked yet
            if i not in known and len(songs[i].difference(songs[curr])) == 0:
                q.append(i) # add to queue if they know all songs that curr person knows

    for i in range(1, n+1):
        if i in known:
            print(i)

if __name__ == '__main__':
    main()
