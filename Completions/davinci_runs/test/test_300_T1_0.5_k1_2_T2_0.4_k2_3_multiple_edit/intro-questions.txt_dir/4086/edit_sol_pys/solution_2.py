
def remove_duplicates(a, n):
    if n == 0 or n == 1:
        return n
    temp = [0] * n
    j = 0
    for i in range(0, n-1):
        if a[i] != a[i+1]:
            temp[j] = a[i]
            j += 1
    temp[j] = a[n-1]
    j += 1
    for i in range(0, j):
        a[i] = temp[i]
    return j
 
a = [1, 2, 2, 3, 4, 4, 4, 5, 5]
n = len(a)
n = remove_duplicates(a, n)
for i in range(n):
    print ("%d" %a[i]),
