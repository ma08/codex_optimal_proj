


def main():
    n = int(input())
    q = list(map(int, input().split()))

    p = []
    p.append(1)
    for i in range(n-1):
        p.append(q[i] + p[i])
    if max(p) > n or min(p) < 1:
        print(-1)
    else:
        print(*p)

main()