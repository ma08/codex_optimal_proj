

def check(n, p, m):
    count = 0
    for i in range(n):
        for j in range(i, n):
            if p[i:j+1].count(m) > 0:
                count += 1
    return count


def main():
    n, m = map(int, input().split())
    p = list(map(int, input().split()))
    print(check(n, p, m))


if __name__ == "__main__":
    main()
