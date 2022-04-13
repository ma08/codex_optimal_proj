import sys

def main(n, m, songs):
    songs = sorted(songs, key=lambda x: x[0] - x[1], reverse=True)
    for i, song in enumerate(songs):
        m -= song[0]
        if m < 0:
            return i
    return n

if __name__ == "__main__":
    print(main())
