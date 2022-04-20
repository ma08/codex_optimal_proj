

def solve(a, b, c):
    if c == 0:
        return 0
    if c == 1:
        return 1+b
    return 1+b+a



if __name__ == "__main__":
    n = int(input())
    a, b, c = [int(x) for x in input().split()]
    print(solve(a, b, c))
