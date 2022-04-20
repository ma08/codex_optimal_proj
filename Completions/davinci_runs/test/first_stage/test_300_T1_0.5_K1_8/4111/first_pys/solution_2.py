

n = int(input())
a = list(map(int, input().split()))

odd_sum = 0
even_sum = 0
good_candy = 0

for i in range(n):
    if i % 2 == 0:
        even_sum += a[i]
    else:
        odd_sum += a[i]

for i in range(n):
    if i % 2 == 0:
        even_sum -= a[i]
    else:
        odd_sum -= a[i]

    if even_sum == odd_sum:
        good_candy += 1

    if i % 2 == 0:
        even_sum += a[i]
    else:
        odd_sum += a[i]

print(good_candy)