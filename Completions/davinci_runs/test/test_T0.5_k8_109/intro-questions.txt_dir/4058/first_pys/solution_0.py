

def main():
    n, r = map(int, input().split())
    house = list(map(int, input().split()))

    # First check if there are any heaters at all
    if sum(house) == 0:
        print(-1)
        return

    # Next check if we can just turn all the heaters on
    if sum(house) + 2*r - 1 == n:
        print(n)
        return

    # Now check if we can warm up the house
    # If we can't, return -1
    # If we can, return the minimum number of heaters we need to turn on
    count = 0
    for i in range(n):
        if house[i] == 1:
            count += 1
            i += 2*r - 1
    if count < n:
        print(-1)
        return
    else:
        # Now we know we can warm up the house
        # We need to turn on heaters at the first and last positions
        # Then we need to turn on a heater at each position that is not warmed up by the previous heater
        # We know we can warm up the house, so we know all the positions in between will be warmed up
        # The minimum number of heaters we need to turn on is the number of intervals between heaters + 1
        # The +1 is for the first and last positions
        count = 1
        for i in range(n):
            if house[i] == 1:
                count += 1
                i += 2*r - 1
        print(count)
        return

if __name__ == '__main__':
    main()