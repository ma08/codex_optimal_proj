# В первой строке записано единственное число n (1 ≤ n ≤ 100) — количество чисел в последовательности

# Во второй строке записаны n чисел a1, a2, ..., an (1 ≤ ai ≤ 109)

# Выведите ответ на задачу

# Sample Input:

# 3
# 1 2 3

# Sample Output:

# 2 1 3

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(a[1], a[0])
elif n == 3:
    if a[0] * 3 == a[1] and a[1] * 2 == a[2]:
        print(a[0], a[1], a[2])
    else:
        print(a[2], a[0], a[1])
else:
    for i in range(n):
        if a[i] % 3 == 0:
            a[i] //= 3
        else:
            a[i] *= 2
    a.sort()
    print(*a)
