def main():
    n, k = map(int, input().split())
    problems = list(map(int, input().split()))
    ans = 0
    for problem in problems:
        if problem <= k:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()
