

n = int(input("Enter the number of elements: "))

a = []

for _ in range(n):
    a.append(int(input("Enter the element: ")))

a.sort()

max_value = 0

for i in range(n):
    current_value = a[i]**2 * (sum(a[i+1:]) + a[i])
    if current_value > max_value:
        max_value = current_value

print(max_value)
