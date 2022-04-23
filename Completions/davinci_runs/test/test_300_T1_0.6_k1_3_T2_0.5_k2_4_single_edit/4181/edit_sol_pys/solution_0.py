

def main(n, monsters):
    monsters.sort()
    total = monsters[0]

    for i in range(1, len(monsters)):
        total += monsters[i] * (i + 1)

    return total

if __name__ == '__main__':
    n = int(input())
    monsters = list(map(int, input().split()))
    print(main(n, monsters))
