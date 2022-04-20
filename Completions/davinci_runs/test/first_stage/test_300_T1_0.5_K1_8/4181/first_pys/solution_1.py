

def main():
    N = int(input())
    monsters_per_town = list(map(int, input().split()))
    monsters_per_town_max = list(map(int, input().split()))

    total_monsters = 0
    for i in range(N):
        total_monsters += min(monsters_per_town[i], monsters_per_town_max[i])
        total_monsters += min(monsters_per_town[i+1], monsters_per_town_max[i] - min(monsters_per_town[i], monsters_per_town_max[i]))
    print(total_monsters)

if __name__ == '__main__':
    main()