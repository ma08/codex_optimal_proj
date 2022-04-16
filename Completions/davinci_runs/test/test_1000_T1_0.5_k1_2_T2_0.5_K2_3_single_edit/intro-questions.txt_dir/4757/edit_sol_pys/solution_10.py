

def main():
    """ Main function """
    num_villagers = int(input())
    num_nights = int(input())
    villagers_nights = []
    for _ in range(num_nights):
        villagers_nights.append(set(map(int, input().split())))
    songs = set()
    for night in range(num_nights):
        if 1 in villagers_nights[night]:
            songs.add(night)
        else:
            for j in range(night):
                if villagers_nights[night].intersection(villagers_nights[j]):
                    songs.add(night)
                    break
    for villager in range(num_villagers):
        if villager == 0 or all(villager in villagers_nights[j] for j in songs):
            print(villager + 1)

main()
