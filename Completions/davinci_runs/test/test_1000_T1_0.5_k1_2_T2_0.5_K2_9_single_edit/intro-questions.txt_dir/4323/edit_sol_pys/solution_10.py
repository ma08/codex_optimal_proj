

import sys

def main():
    n, m = map(int, input().split())
    songs = []
    for i in range(n):
        a, b = map(int, input().split())
        songs.append(a-b)
    songs = sorted(songs, reverse=True)
    total = 0
    for i, song in enumerate(songs):
        if song > 0:
            total += song
            if total <= m:
                return i + 1
    return n

if __name__ == "__main__":
    print(main())
