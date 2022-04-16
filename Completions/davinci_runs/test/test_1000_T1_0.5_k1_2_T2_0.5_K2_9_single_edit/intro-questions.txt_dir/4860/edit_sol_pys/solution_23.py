

n = int(input("Enter the number of elements: "))

for i in range(n):
    x = int(input("Enter element: "))
    if i == 0:
        low = 1
        high = x
    else:
        low = high + 1
        high = x

for i in range(low, high+1):
    print(i)
