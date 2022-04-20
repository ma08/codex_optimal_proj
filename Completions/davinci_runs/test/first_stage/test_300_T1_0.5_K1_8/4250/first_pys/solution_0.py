

def main():
    n, k = map(int, input().split())
    s = list(map(int, input().split()))

    t = [0 for _ in range(k)]
    for i in range(k):
        t[i] = max(s)
        s.remove(t[i])

    print(" ".join(map(str, t)))


main()