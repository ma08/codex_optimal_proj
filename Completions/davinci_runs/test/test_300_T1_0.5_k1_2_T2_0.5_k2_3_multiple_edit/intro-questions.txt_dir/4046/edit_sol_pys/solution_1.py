

# function to calculate the permutation

def solve(n, q):
    p = [1]
    for i in range(n - 1):
        if p[-1] + q[i] > 0 and p[-1] + q[i] <= n:
            p.append(p[-1] + q[i])
        else:
            return -1
    return p
# main function


def main():
    n = int(input())
    q = [int(x) for x in input().split()]
    print(*solve(n, q))


if __name__ == "__main__":
    main()
