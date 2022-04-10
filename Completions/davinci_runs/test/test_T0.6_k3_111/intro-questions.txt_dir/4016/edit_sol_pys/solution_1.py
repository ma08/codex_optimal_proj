

from collections import Counter

def main():
    n, k = map(int, input().split())
    t = input()

    c = Counter(t)
    c = sorted(c.items(), key=lambda x: x[0])

    h = []
    for i in range(0, len(c), 2):
        h.append(c[i])
        h.append(c[i + 1])

    s = []
    for i in range(len(h)):
        s.append(h[i][0] * (n // 2))

    for i in h[::-1][1:]:
        s.append(i[0] * (n // 2 + n % 2))

    s = "".join(s)

    if k == 1:
        print(t)
    elif k == 2:
        print(s)
    else:
        print(s * (k - 2) + s[:n])

main()
