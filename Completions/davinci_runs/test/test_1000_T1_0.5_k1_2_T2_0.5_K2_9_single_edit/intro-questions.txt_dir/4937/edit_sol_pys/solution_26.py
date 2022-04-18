def main():
    n, a = map(int, input().split())
    l = list(map(int, input().split()))
    l.sort()
    i = 0
    while a > 0 and i < n:
        if a >= l[i]:
            a -= l[i]
            i += 1
        else:
            break
    print(i)


def main():
    n, a = map(int, input().split())
    e = list(map(int, input().split()))
    e.sort()
    i = 0
    while a > 0 and i < n:
        if a >= e[i]:
            a -= e[i]
            i += 1
        else:
            break
    print(i)

if __name__ == "__main__":
    main()
