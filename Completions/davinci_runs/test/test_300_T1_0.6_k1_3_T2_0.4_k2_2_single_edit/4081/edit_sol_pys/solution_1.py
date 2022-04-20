

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [0] * (n + 1)
    stack = []
    for i in range(1, n + 1):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = i
        stack.append(i)
    for i in range(n, 0, -1):
        while stack and nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = i
        stack.append(i)
    max_ans = 0
    for i in range(1, n + 1):
        max_ans = max(max_ans, ans[i] - i + 1)
    print(max_ans)
    for i in range(1, n + 1):
        if i == n - 1 or ans[i] < ans[i + 1]:
            print('L', end='')
        else:
            print('R', end='')
    print()

main()
