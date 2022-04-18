

def solve(a):
    m = min(a)

    factors = []
    for i in range(1, m+1):
        if m % i == 0:
            factors.append(i)

    for i in range(len(factors)):
    count = 0
        if factors[i] != 0:
            for j in range(len(a)):
                if a[j] % factors[i] != 0:
                    factors[i] = 0
                    break
            if factors[i] != 0:
                count += 1

    return count


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
