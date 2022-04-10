

def main():
    n, x, y = map(int, input().split())
    s = input()
    ans = 0
    for i in range(n-1, max(n-x-1, 0), -1):
        if s[i] == "0":
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()