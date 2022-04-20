

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x.sort()
    ans = 0
    for i in range(n):
        if x[i] < x[0]:
            ans += x[0] - x[i]
        elif x[i] > x[0]:
            ans += x[i] - x[0] - 1
    print(ans)

if __name__ == "__main__":
    main()