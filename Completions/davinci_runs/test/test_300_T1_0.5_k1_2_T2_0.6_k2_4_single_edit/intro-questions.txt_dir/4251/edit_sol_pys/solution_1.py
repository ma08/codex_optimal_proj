from fractions import gcd


def main():
    a, b, c, d = map(int, input().split())
    print(solve(a, b, c, d))


def solve(a, b, c, d):

    # First, find the number of integers between a and b that are divisible by c
    num_divisible_by_c = b // c - (a - 1) // c
    # Now, find the number of integers between a and b that are divisible by d
    num_divisible_by_d = b // d - (a - 1) // d
    # Next, find the number of integers between a and b that are divisible by both c and d
    num_divisible_by_cd = b // (c * d) - (a - 1) // (c * d)
    # Then, find the number of integers between a and b that are divisible by lcm(c, d)
    num_divisible_by_lcm = b // (c * d // gcd(c, d)) - (a - 1) // (c * d // gcd(c, d))
    return num_divisible_by_lcm - num_divisible_by_cd


if __name__ == "__main__":
    main()
