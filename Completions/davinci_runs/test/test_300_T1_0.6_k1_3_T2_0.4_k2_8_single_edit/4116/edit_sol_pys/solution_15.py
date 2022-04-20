

n = int(input())
if n == 1:
    print("Yes")
elif n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
    print("No")
else:
    print("No")
