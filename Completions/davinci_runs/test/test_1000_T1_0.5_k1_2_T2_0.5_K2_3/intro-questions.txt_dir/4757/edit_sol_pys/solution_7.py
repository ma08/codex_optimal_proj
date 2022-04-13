

import sys

def main():
    n = int(sys.stdin.readline().strip())
    songs = {}
    for i in range(n):
        line = sys.stdin.readline().strip().split()
        k = int(line[1])
        songs[line[0]] = k
    for i in range(n):
        print(songs[i])

main()
