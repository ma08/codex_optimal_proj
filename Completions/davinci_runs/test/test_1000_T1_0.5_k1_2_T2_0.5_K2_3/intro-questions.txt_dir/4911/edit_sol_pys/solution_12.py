from sys import stdin, stdout



    songs = []
def main():
    n = int(stdin.readline())
    for i in range(n):
        songs.append(stdin.readline().strip())
    songs.sort()
    for song in songs:
        stdout.write(song + '\n')


main()
