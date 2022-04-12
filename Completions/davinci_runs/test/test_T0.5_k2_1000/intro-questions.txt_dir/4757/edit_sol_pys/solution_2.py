
import sys

def main():
    villagers = int(sys.stdin.readline().strip())  # read the first line
    evenings = int(sys.stdin.readline().strip())
    songs = []
    for evening in range(evenings):
        singers = [int(x) for x in sys.stdin.readline().strip().split()]
        if singers[0] == 1:
            songs.append(singers[1])
        else:
            songs.extend(singers[1:])
    for villager in range(1, villagers+1):
        if songs.count(villager) == len(songs):
            print(villager)

if __name__ == '__main__':
    main()
