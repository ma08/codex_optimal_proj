
import random

def fight(monster_list):
    while len(monster_list) > 1:
        attacker = random.choice(monster_list)
        monster_list.remove(attacker)
        defender = random.choice(monster_list)
        defender[0] -= attacker[0]
        if defender[0] <= 0:
            monster_list.remove(defender)
    return monster_list[0][0]

def main():
    N = int(input())
    A = list(map(int, input().split()))
    monster_list = []
    for i in range(N):
        monster_list.append([A[i], i])
    print(fight(monster_list))

if __name__ == '__main__':
    main()