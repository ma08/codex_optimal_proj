

def main():
    """ Main function """
    num_villagers, num_nights = map(int, input().split())
    villagers_night = [set(map(int, input().split())) for _ in range(num_nights)]
    songs = set(i for i in range(num_nights) if 1 in villagers_night[i])
    for i in range(1, num_villagers):
        if all(i in villagers_night[j] for j in songs):
            print(i)

main()
