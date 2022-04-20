

def main():
    n = int(input())
    nums = list(map(int, input().split()))
    ans = [-1] * n
    stack = []
    for i in range(n):
        while stack and nums[stack[-1]] <= nums[i]:
            ans[stack[-1]] = i
            stack.pop()
        stack.append(i)
    for i in range(n - 1, -2, -1):
        while stack and nums[stack[-1]] <= nums[i]:
            ans[stack[-1]] = i
            stack.pop()
        stack.append(i)
    max_ans = 0
    for i in range(n):
        max_ans = max(max_ans, ans[i] - i)
    print(max_ans)
    for i in range(n):
        if i == n - 1 or ans[i] < ans[i + 1]:
            print('L', end='')
        else:
            print('R', end='')
    print()

main()
