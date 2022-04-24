
def solve(n, k, s):
    i = 0
    routers = 0
    cost = 0
    while i < n:
        if s[i] == '1':
            routers += 1
            cost += i
            i += k * 2 + 1
        else:
            cost += i
            i += 1
    return cost

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
