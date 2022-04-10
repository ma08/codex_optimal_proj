

def solve(rooms, k, s):
    cost = 0
    routers = 0
    for i in range(rooms):
        if s[i] == '1':
            routers += 1
        elif i > 0 and s[i-1] == '1':
            routers -= 1
        if i >= k and s[i-k] == '1':
            routers += 1
        if routers == 0:
            cost += i+1
    return cost

if __name__ == '__main__':
    n, k = map(int, input().split())
    s = input()
    print(solve(n, k, s))