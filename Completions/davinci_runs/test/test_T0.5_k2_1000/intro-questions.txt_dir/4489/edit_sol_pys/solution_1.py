

def main():
    n = int(input())  # 1行目
    s = [input() for _ in range(n)]  # 2行目以降
    m = int(input())  # 1行目
    t = [input() for _ in range(m)]  # 2行目以降

    ans = 0
    for si in s:
        if si in t:
            ans -= 1
        else:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()
