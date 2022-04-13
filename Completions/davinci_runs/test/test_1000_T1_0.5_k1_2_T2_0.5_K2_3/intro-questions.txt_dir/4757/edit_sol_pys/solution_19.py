

import sys

def main():
    n = int(sys.stdin.readline().strip())
    e = int(sys.stdin.readline().strip())
    songs = []
    for i in range(e):
        line = sys.stdin.readline().strip().split()
        songs.append(line[1:])
    for i in range(1, n + 1):
        print(i)

main()
