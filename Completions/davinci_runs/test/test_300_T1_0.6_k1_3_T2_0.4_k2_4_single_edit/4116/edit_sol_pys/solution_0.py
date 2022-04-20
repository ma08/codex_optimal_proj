

n = int(input("Enter n: "))

for i in range(1, n+1):
    if i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
        print("Yes")
    elif i == 1:
        print("Yes")
    else:
        print("No")
