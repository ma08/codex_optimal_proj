
import sys

def main():
    n = int(sys.stdin.readline().strip())
    e = int(sys.stdin.readline().strip())
    songs = []
    for i in range(e):
        line = sys.stdin.readline().strip().split()
        for j in range(1, int(line[0]) + 1):
            songs.append(line[j])
    for i in range(1, n + 1):
        print(songs[i - 1])

main()
