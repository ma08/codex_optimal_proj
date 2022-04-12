

def find_min_rooms(minions):
    # Use a greedy algorithm
    # For each minion, find the lowest temperature that is available in the rooms
    # If none is available, create a new room with that temperature and put the minion in it

    rooms = []

    for i in range(len(minions)):
        m = minions[i]
        available = False
        for r in rooms:
            if m[0] <= r <= m[1]:
                available = True
                break
        if not available:
            rooms.append(m[0])

    return len(rooms)


if __name__ == '__main__':
    n = int(input())
    minions = []

    for i in range(n):
        l, u = map(int, input().split())
        minions.append((l, u))

    print(find_min_rooms(minions))
