

def main():
    n = int(input())
    monsters = list(map(int, input().split()))
    heroes = list(map(int, input().split()))

    monsters.sort()
    heroes.sort()

    for monster in monsters[::-1]:
        for hero in heroes[::-1]:
            if monster <= hero:
                heroes.remove(hero)
                break
        else:
            print("NO")
            return

    print("YES")


if __name__ == '__main__':
    main()
