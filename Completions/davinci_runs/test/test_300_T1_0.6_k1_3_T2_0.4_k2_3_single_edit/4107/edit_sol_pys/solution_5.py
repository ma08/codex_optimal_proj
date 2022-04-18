

def solve(n, k, s):
    i = 1
    routers = 0
    cost = 0
    while i <= n:
        # print("i: {}".format(i))
        if s[i-1] == '1' and routers < k:
            # print("router at {}".format(i))
            routers += 1
            cost += i
            i += 2*k + 1
        else:
            # print("connection at {}".format(i))
            i += 1
    # print("routers: {}".format(routers))
    return cost

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))
