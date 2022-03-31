

def solve(n, divs):
    mx = max(divs)
    divs.remove(mx)
    sums = {}
    for d in divs:
        for e in divs:
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