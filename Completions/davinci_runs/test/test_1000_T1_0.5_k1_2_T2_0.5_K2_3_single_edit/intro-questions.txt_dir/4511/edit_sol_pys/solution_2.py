
def get_damage(turns):
    damage = 0
    for turn in range(turns):
        cards = int(input())
        costs = []
        for _ in range(cards):
            costs.append(list(map(int, input().split())))
        costs.sort(key=lambda x: x[1], reverse=True)
        turn_damage = 0
        for i in range(len(costs)):
            if i % 10 == 0:
                turn_damage += 2 * costs[i][1]
            else:
                turn_damage += costs[i][1]
            if sum([cost[0] for cost in costs[:i + 1]]) > 3:
                break
        damage += turn_damage
    print(damage)


if __name__ == '__main__':
    turns = int(input())
    get_damage(turns)
