

def main(n, monsters, heroes):
    monsters.sort(reverse = True)
    heroes.sort(reverse = True)
    total = 0

    hero = 0
    for monster in monsters:
        if hero >= len(heroes):
            break
        if monster > heroes[hero]:
            total += monster
        else:
            total += heroes[hero]
            hero += 1

    return total

if __name__ == '__main__':
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))
    print(main(n, monsters, heroes))
