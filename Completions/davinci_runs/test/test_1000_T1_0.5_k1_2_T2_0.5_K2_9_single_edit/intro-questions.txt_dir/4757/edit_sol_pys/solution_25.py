

def main():
    """ Main function """
    num_villagers = int(input())
    num_nights = int(input())
    villagers_nights = []
    for _ in range(num_nights):
        villagers_nights.append(set(map(int, input().split())))
    songs = set()
    for i in range(num_nights):
        if 0 in villagers_nights[i]:
            songs.add(i)
        else:
            for j in range(i):
                if villagers_nights[i].intersection(villagers_nights[j]) != set():
                    songs.add(i)
                    break
    for i in range(num_villagers):
        if i == 0 or all(i in villagers_nights[j] for j in songs):
            print(i + 1)

main()
