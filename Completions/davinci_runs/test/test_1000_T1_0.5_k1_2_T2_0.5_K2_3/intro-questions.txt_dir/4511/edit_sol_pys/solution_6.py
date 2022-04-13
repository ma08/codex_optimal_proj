
import sys

def main():
    n = int(input())
    turn_dict = {i: [] for i in range(n)}
    for i in range(n):
        k = int(input())
        for j in range(k):
            c, d = map(int, input().split())
            turn_dict[i].append((c, d))
    damage = 0
    for i in range(n):
        turn_dict[i].sort(key=lambda x: x[1], reverse=True)
        turn_cost = 0
        turn_damage = 0
        for card in turn_dict[i]:
            if turn_cost + card[0] <= 3:
                turn_cost += card[0]
                if turn_cost % 10 == 0:
                    turn_damage += card[1] * 2 
                else:
                    turn_damage += card[1]
        damage += turn_damage
    print(damage)

if __name__ == "__main__":
    main()
