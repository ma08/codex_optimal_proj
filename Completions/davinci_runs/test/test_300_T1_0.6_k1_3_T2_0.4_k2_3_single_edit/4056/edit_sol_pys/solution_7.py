

def solve(a):
    m = max(a)
    if m == 2:
        return 1

    factors = [2, 3, 5, 7]
    for i in range(8, m+1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            factors.append(i)

    for i in range(len(factors)-1, -1, -1):
        for j in range(len(a)):
            if a[j] % factors[i] == 0:
                factors.pop(i)
                break


    return len(factors)


if __name__ == "__main__":
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(a))
