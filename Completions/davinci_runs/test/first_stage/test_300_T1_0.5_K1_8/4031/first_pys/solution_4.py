

# Solution

def solve(n, arr):
    arr.sort(key=len)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] not in arr[j]:
                return 'NO'
    return 'YES\n' + '\n'.join(arr)


n = int(input())
arr = [input() for _ in range(n)]
print(solve(n, arr))