from sys import stdin


def main():
    n = int(stdin.readline())
    while n != 0:
        songs = []
        for i in range(n):
            songs.append(stdin.readline().strip())
        songs.sort()
        for song in songs:
            print(song)
        n = int(stdin.readline())
        if n != 0:
            print()


main()
