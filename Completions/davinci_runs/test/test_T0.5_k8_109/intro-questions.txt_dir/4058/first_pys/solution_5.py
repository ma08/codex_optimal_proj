

def main():
    n, r = map(int, input().split())
    house = list(map(int, input().split()))
    heaters = 0
    for i in range(n):
        if house[i] == 1:
            heaters += 1
            for j in range(i-r+1, i+r):
                if j >= 0 and j < n:
                    house[j] = 2
    if 1 in house:
        print(-1)
    else:
        print(heaters)

if __name__ == "__main__":
    main()