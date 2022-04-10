# https://atcoder.jp/contests/abc077/tasks/arc084_a


def main():
    n, r = map(int, input().split())
    a, b = [], []
    for _ in range(n):
        a_i, b_i = map(int, input().split())  # a_i, b_i = list(map(int, input().split()))
        a.append(a_i)  # a.append(list(map(int, input().split()))
        b.append(b_i)  # b.append(list(map(int, input().split()))

    # print(a)
    # print(b)

    for i in range(n):
        if r < a[i]:
            print("NO")
            break
        r += b[i]
        if r < 0:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    main()
