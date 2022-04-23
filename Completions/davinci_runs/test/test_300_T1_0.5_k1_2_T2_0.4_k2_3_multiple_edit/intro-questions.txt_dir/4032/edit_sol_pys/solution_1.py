
def main():
    n, k = map(int, input().split())  # n:問題数 k:難易度
    problems = list(map(int, input().split()))
    ans = 0  # 回答可能問題数
    while len(problems) > 0:
        if problems[0] <= k:  # 先頭の問題が解ける
            ans += 1
            problems.pop(0)
        elif problems[-1] <= k:  # 末尾の問題が解ける
            ans += 1
            problems.pop()
        else:
            break
    print(ans)


if __name__ == '__main__':
    main()
