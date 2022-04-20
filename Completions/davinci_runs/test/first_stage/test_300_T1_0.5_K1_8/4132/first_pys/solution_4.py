

import random

def main():
    n = int(input())
    a = list(map(int, input().split()))

    while len(a) > 1:
        a.sort()
        attacker = a.pop()
        defender = random.choice(a)
        a.remove(defender)
        if attacker > defender:
            a.append(attacker - defender)

    print(a[0])

if __name__ == '__main__':
    main()