

N = int(input())
problems = list(map(int, input().split()))

problems.sort()

left = 0
right = N - 1

while left < right:
    if problems[left] + problems[right] == 10:
        left += 1
        right -= 1
    elif problems[left] + problems[right] > 10:
        right -= 1
    else:
        left += 1

print(right - left)