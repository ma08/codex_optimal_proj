

def main():
    n, k = map(int, input().split())  # n: 問題数, k: 時間
    problems = list(map(int, input().split()))  # 問題リスト
    ans = 0
    while len(problems) > 0:
        if problems[0] <= k:
            ans += 1
            problems.pop(0)
        elif problems[-1] <= k:
            ans += 1
            problems.pop()
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
