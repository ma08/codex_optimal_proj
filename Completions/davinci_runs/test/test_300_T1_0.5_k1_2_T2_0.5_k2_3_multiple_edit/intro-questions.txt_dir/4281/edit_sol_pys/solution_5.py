import fractions


def main():
    a, b, c, d = map(int, input().split())
    a -= 1
    c -= 1
    lcm = b * d // fractions.gcd(b, d)
    ans = b + d - lcm
    ans -= b * (a // b)
    ans -= d * (c // d)
    ans += lcm * ((a + c) // lcm)
    print(ans)


if __name__ == "__main__":
    main()
