

def solve(n, a):
    res = [0]*n
    stack = []
    for i in range(n):
        while len(stack) > 0 and stack[-1][0] < a[i]:
            res[stack[-1][1]] = i+1
            stack.pop()
        stack.append((a[i], i))
    while len(stack) > 0:
        res[stack[-1][1]] = stack[-1][1]+1
        stack.pop()
    cur = 0
    ans = [0]*n
    for i in range(n):
        if res[i] > cur:
            ans[i] = 'L'
            cur = res[i]
        else:
            ans[i] = 'R'
    return ''.join(ans)

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    print(solve(n, a))

if __name__ == '__main__':
    main()