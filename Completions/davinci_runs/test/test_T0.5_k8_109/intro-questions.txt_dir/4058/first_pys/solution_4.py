

def main():
    n, r = map(int, input().split())
    house = list(map(int, input().split()))
    heaters = 0
    warmed_up = []
    for i in range(len(house)):
        if house[i] == 1:
            warmed_up.extend(range(i-r+1, i+r))
    warmed_up = set(warmed_up)
    if len(warmed_up) == n:
        print(sum(house))
    else:
        print(-1)



if __name__ == "__main__":
    main()