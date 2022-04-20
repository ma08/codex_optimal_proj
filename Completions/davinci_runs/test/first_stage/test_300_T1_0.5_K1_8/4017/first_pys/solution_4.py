

# SOLUTION
def is_good(arr):
    return len(arr) == 1 or sum(arr[1:]) == arr[0]

n = int(input())
arr = list(map(int, input().split()))

res = []
for i in range(n):
    if is_good(arr[:i] + arr[i+1:]):
        res.append(i+1)

print(len(res))
print(*res)