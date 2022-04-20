import heapq



def main(n, monsters, heroes):
    heapq.heapify(monsters)
    heapq.heapify(heroes)
    total = 0

    hero = 0
    for monster in monsters:
        if hero >= len(heroes):
            break
        if monster > heroes[0]:
            total += monster
        else:
            total += heroes[0]
            heapq.heappop(heroes)
            hero += 1

    return total

if __name__ == '__main__':
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))
    print(main(n, monsters, heroes))
