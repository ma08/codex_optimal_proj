

def main():
    a, b, c = [int(i) for i in input().split()]

    ans = 0

    if a == b:
        ans += 1

    if b == c:
        ans += 1

    if c == a:
        ans += 1

    print(ans)


main()
