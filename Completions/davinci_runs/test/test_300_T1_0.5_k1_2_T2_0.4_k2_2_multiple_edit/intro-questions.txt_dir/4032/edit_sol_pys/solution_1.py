
def main():
    n, k = map(int, input().split())
    problems = sorted(list(map(int, input().split())))
    ans = 0
    for p in problems:
        if p > k:
            break 
        ans += 1
        k -= p
    print(ans)


if __name__ == '__main__':
    main()
