

n = int(input())
arr = list(map(int, input().split()))

for i in range(n):
    if n == 2:
        if arr[0] % 3 == 0:
            print(arr[0], arr[1])
        else:
            print(arr[1], arr[0])
        break
    elif arr[i] % 3 == 0:
        for j in range(n):
            if arr[j] * 2 == arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                break

arr = list(map(str, arr))
print(' '.join(arr))