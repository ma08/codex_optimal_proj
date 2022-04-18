
def main():
    n, m = map(int, input().split())
    songs = []
    for i in range(n):
        a, b = map(int, input().split())
        songs.append(a - b)
    songs = sorted(songs, reverse=True)
    total = 0
    for i in range(n):
        total += songs[i]
        if total <= m:
            return i + 1
    return -1

if __name__ == "__main__":
    print(main())
