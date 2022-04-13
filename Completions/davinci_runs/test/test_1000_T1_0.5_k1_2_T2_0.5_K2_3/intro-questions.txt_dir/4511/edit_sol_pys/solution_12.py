

def main():
    n = int(input())
    turn_dict = {}
    for _ in range(n):
        k = int(input())
        turn_dict[_] = []
        for j in range(k):
            c, d = [int(x) for x in input().split()]
            turn_dict[_].append((c, d))
    damage = 0
    for _ in range(n):
        turn_dict[_].sort(key=lambda x: x[1], reverse=True)
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
