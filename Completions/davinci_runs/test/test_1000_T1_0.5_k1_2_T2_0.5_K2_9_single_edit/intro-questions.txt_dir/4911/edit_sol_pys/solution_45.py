
import sys

class Song:
    def __init__(self, attrs):
        self.attrs = attrs
    def __repr__(self):
        return ' '.join(self.attrs)

def stable_sort(songs, attribute):
    return sorted(songs, key=lambda song: song.attrs[attribute])

def main():
    attrs = sys.stdin.readline().strip().split()
    m = int(sys.stdin.readline())
    songs = []
    for _ in range(m):
        songs.append(Song(sys.stdin.readline().strip().split()))
    n = int(sys.stdin.readline())
    for _ in range(n):
        attribute = sys.stdin.readline().strip()
        print(' '.join(attrs))
        for song in stable_sort(songs, attrs.index(attribute)):
            print(song)
        print()

if __name__ == '__main__':
    main()
