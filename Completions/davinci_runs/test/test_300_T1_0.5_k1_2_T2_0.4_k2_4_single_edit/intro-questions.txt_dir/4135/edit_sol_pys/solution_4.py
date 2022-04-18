

n = int(input("Enter the number of elements: "))
t = input("Enter the elements: ")

s = [0] * n

for i in range(n):
    s[i] = int(t[i])

print(s)

for i in range(n):
    for j in range(i + 1, n):
        if s[i] > s[j]:
            temp = s[i]
            s[i] = s[j]
            s[j] = temp

print(s)
