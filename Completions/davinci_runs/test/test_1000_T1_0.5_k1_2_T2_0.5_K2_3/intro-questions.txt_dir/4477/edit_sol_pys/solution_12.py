def solve(c):
    r = 0
    for i in range(len(c)):
        r += int(c[i])
        r += 1
    return r


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        c = input()
        print(solve(c))
