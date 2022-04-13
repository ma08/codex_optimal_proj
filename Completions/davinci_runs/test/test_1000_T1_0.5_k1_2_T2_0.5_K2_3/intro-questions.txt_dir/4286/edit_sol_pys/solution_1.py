

def main():
    n = int(input())
    a = list(map(int, input().split(" ")))

    min_cost = 0
    for i in range(n):
        min_cost += a[i]

    for i in range(n):
        for j in range(i):
            if a[i] == a[j]:
                min_cost -= a[i]

    print(min_cost)


if __name__ == "__main__":
    main()
