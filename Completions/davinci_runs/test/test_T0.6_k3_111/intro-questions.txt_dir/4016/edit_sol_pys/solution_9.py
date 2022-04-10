

def main():
    n, k = map(int, input().split())
    t = input()

    c = list(t)
    c.sort()

    s = "".join(c[:n // 2]) + "".join(c[:n // 2][::-1])

    if k == 1:
        print(t)
    elif k == 2:
        print(s)
    else:
        print(s * (k - 2) + s[:n])

main()
