

import sys

def main():
    villagers = int(sys.stdin.readline().strip()) # number of villagers
    evenings = int(sys.stdin.readline().strip()) # number of evenings
    songs = []
    for evening in range(evenings):
        singers = [int(x) for x in sys.stdin.readline().strip().split()] # list of singers for each evening
        if singers[0] == 1:
            songs.append(singers[1]) # if only one singer, add to list
        else:
            songs.extend(singers[1:]) # if multiple singers, add to list
    for villager in range(1,villagers+1):
        if songs.count(villager) == len(songs): # if villager sang every evening, print
            print(villager)

if __name__ == '__main__':
    main()
