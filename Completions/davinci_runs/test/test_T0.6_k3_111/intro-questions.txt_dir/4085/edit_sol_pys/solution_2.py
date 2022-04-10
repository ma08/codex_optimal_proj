

def solve(n, divisors):
    mx = max(divisors)
    divisors.remove(mx)
    sums = {}
    for d in divisors:
        for e in divisors:
            s = d + e
            if s in sums:
                return mx * s
            sums[s] = True
    return -1


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        divs = [int(x) for x in input().split()]
        print(solve(n, divs)) 


if __name__ == "__main__":
    main()
