
def solve(n, k, s):
    routers = 0
    cost = 0
    for i, c in enumerate(s, 1):
        if c == '1':
            routers += 1
            cost += i
            i += k * 2
        else:
            cost += i
            i += 1
    return cost


if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
