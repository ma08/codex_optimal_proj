
def solve(a, b):
    if a == 0:
        return 'No'
    if a == 1:
        return 'Yes'
    if b == 0:
        return 'No'
    return solve(a % b, b % a)
a, b = map(int, input().split())
print(solve(a, b))
