

def main():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        ans = n // k
        if n % k != 0:
            ans += 1
        print(ans)

if __name__ == "__main__":
    main()