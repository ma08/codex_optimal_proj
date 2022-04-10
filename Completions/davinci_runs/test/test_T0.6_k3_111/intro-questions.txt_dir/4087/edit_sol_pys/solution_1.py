

# In: integer, integer
# Out: integer

a, b = map(int, input().split())

if a > b:
    a, b = b, a

if a % 2 == 0:
    a += 1

sum_odd = 0

for i in range(a, b + 1, 2):
    sum_odd += i

print(sum_odd)
