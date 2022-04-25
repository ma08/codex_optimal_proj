# pythoneer

n = int(input("Enter the number of elements in the list: "))
a = list(map(int, input("Enter the elements of the first list: ").split()))
b = list(map(int, input("Enter the elements of the second list: ").split()))

c = [0] * n
for i in range(n):
    c[(a[i] + b[i]) % n] += 1 # c[i] = c[i] + 1

for i in range(n):
    for j in range(c[i]):
        print(i, end=" ")
