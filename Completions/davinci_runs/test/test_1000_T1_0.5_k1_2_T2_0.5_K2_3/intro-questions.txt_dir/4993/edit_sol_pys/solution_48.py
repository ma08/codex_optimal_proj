


def main():
    parts, days = map(int, input().split())
    boat_parts = []
    for _ in range(days):
        boat_parts.append(input())
    boat_parts_set = set(boat_parts)
    if len(boat_parts_set) < parts:
        print('paradox avoided')
        return
    for i, boat_part in enumerate(boat_parts):
        if boat_part in boat_parts_set:
            boat_parts_set.remove(boat_part)
            if not boat_parts_set:
                print(i+1)
                return



if __name__ == '__main__':
    main()
