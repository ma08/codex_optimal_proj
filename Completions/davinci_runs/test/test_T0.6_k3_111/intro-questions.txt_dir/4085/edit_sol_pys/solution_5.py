

def solve(n, divs):
    if n == 1:
        return -1
    if n == 2:
        return divs[0] * divs[1]
    if n == 3:
        return max(divs[0] * divs[1], divs[0] * divs[2], divs[1] * divs[2])
    if n == 4:
        return max(divs[0] * divs[1] + divs[2] * divs[3], divs[0] * divs[2] + divs[1] * divs[3], divs[0] * divs[3] + divs[1] * divs[2])


def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        divs = [int(x) for x in input().split()]
        print(solve(n, divs))


if __name__ == "__main__":
    main()
