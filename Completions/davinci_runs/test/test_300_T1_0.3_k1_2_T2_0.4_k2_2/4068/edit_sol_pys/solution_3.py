
def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    b = list(map(int, input().split()))
    b.sort()
    c = list(map(int, input().split()))
    c.sort()


    ans = 0
    for bb in b:
        ans += bisect_left(a, bb) * (n - bisect_right(c, bb))
    print(ans)


if __name__ == '__main__':
    main()
