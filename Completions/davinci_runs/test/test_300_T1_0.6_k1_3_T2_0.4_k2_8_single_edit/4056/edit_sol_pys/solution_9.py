


def solve(a):
    m = min(a)
    if m == 1:
        return 1

    factors = []
    for i in range(2, m + 1):
        if m % i == 0:
            factors.append(i)

    # for i in range(len(factors)):
    #     for j in range(len(a)):
    #         if a[j] % factors[i] != 0:
    #             factors[i] = 0
    #             break

    return factors


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
