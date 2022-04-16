import sys



def main():
    attributes = sys.stdin.readline().rstrip().split()
    songs = []
    for i in range(int(sys.stdin.readline())):
        songs.append(sys.stdin.readline().rstrip().split())
    for i in range(int(sys.stdin.readline())):
        attribute = sys.stdin.readline().rstrip()
        songs.sort(key=lambda x: x[attributes.index(attribute)])
        print(' '.join(attributes))
        for song in songs:
            print(' '.join(song))
        print()


main()
