from math import ceil

def find_min_arr(n, k):
    arr = [1] * k
    for i in range(k-1, -1, -1): # Проходим от конца к началу
        if sum(arr) > n:
            arr[i] -= sum(arr) - n # Если сумма больше, то уменьшаем на разницу
        if arr[i] == 0:
            return False
        if i == 0:
            break
        if arr[i] > arr[i-1] * 2: # Если предыдущий элемент меньше текущего в 2 раза, то увеличиваем на 1
            arr[i-1] = arr[i] // 2 + 1
    return arr

n, k = [int(x) for x in input().split()]
arr = find_min_arr(n, k)
if arr:
    print("YES")
    print(*arr)
else:
    print("NO")
