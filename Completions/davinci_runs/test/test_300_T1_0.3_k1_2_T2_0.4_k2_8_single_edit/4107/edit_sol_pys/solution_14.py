

def main():
    n, k = map(int, input().split())
    s = input()
    cost = 0
    for i in range(n):
        cost += min(i + 1, n - i)
    print(cost)

if __name__ == "__main__":
    main()
