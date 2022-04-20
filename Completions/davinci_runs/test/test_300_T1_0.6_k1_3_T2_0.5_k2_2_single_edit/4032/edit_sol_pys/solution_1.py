n = int(input())
a = [int(x) for x in input().split()]


b = []
for i in range(n-1):
    b.append(abs(a[i] - a[i+1]))

solved = 0
i, j = 0, n-1
while i <= j:
    solved += 1
    if a[i] <= k and a[j] <= k:
        if a[i] < a[j]:
            i += 1
        elif a[i] > a[j]:
            j -= 1
        else:
            i += 1
    elif a[i] > k and a[j] <= k:
        j -= 1
    elif a[i] <= k and a[j] > k:
        i += 1
    else:
        break
print(solved)
