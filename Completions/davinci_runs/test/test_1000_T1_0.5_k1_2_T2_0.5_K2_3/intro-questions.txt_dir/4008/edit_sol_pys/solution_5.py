
def main():
    n = int(input())
    a = [list(map(int, input().split())) for _ in range(n)]
    a.sort(key=lambda x: (x[0], x[1]))
    ans = 0
    while a:
        x, y = a.pop()
        if ans == 0:
            ans = y
        else:
            if ans > y:
                ans = y
    print(ans)


if __name__ == '__main__':
    main()
