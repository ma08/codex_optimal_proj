
def solve(s, t):
    return abs(len(s) - len(t))


if __name__ == "__main__":
    s = input()
    t = input()
    print(solve(s, t))
