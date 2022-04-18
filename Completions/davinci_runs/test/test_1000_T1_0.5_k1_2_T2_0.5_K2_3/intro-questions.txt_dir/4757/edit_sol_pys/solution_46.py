

def main():
    """ Main function """
    num_villagers = int(input())
    num_nights = int(input())
    villagers_night = []
    for _ in range(num_nights):
        villagers_night.append(set(map(int, input().split())))
    songs = set()
    for i in range(num_nights):
        if 1 in villagers_night[i]:
            songs.add(i)
        else:
            for j in range(i):
                if villagers_night[i].intersection(villagers_night[j]):
                    songs.add(i)
                    break
    for i in range(num_villagers):
        if i == 0 or all(i + 1 in villagers_night[j] for j in songs):
            print(i + 1)

main()
