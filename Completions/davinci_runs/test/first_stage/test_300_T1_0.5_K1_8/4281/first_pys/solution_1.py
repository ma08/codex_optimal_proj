

def main():
    n = int(input())
    x = list(map(int, input().split()))
    min_houses = max_houses = 1
    for i in range(1, n):
        if x[i] == x[i-1] + 1:
            min_houses += 1
        elif x[i] == x[i-1] - 1:
            max_houses += 1
    print(min_houses, max_houses)

if __name__ == "__main__":
    main()