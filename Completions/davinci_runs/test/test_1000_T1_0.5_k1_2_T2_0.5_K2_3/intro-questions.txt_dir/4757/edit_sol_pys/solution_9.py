

def main():
    """ Main function """
    num_villagers = int(input()) # input number of villagers
    num_nights = int(input()) # input number of nights
    villagers_night = []
    for _ in range(num_nights):
        villagers_night.append(set(map(int, input().split()))) # input villagers per night
    songs = set()
    for i in range(num_nights):
        if 1 in villagers_night[i]: # if the villager 1 is in the input villager set, add the night
            songs.add(i)
        else:
            for j in range(i): # if the villager 1 isn't in the input villager set, check if there is a intersection between the current night and the nights before
                if villagers_night[i].intersection(villagers_night[j]):
                    songs.add(i)
                    break
    for i in range(num_villagers):
        if i == 0 or all(i in villagers_night[j] for j in songs): # print the villager number if it is the villager 1 or if the villager is in all the night that villager 1 is in
            print(i + 1)

main()
