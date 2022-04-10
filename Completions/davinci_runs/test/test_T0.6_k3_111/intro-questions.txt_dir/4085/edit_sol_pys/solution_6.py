

def solve(n, divs):
    divs.sort()
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if divs[i] + divs[j] > divs[k]:
                    return divs[i] + divs[j] + divs[k]
    return 0


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        divs = [int(x) for x in input().split()]
        print(solve(n, divs))


if __name__ == "__main__":
    main()
