

from collections import Counter

def main():
    n, k = map(int, input().split())
    t = input()

    c = Counter(t)
    c = sorted(c.items(), key=lambda x: x[1])

    h = []  # half
    for i in range(0, len(c)):
        h.append(c[i][0])

    s = []  # string
    for i in range(0, len(h)):
        s.append(h[i] * (n // 2))
        s.append(h[-i - 1] * (n // 2))

    s = "".join(s)

    if k == 1:
        print(t)
    elif k == 2:
        print(s)
    else:
        print(s * (k - 2) + s[:n])

main()
