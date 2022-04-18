

def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    e.sort()
    ans = 0
    while a > 0:
        ans += 1
        a -= e.pop()
    print(ans)

if __name__ == "__main__":
    main()
