

n = int(input())

a = []

for _ in range(n):
    a.append(int(input()))

a.sort()

max_value = 0

for i in range(n):
    current_value = a[i]**2 * (sum(a[i+1:]) + a[i]**2)
    if current_value > max_value:
        max_value = current_value

print(max_value)
