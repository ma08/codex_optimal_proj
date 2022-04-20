

n = int(input())
if n % 2 == 0 and n > 2:
    print("Yes")
elif n % 3 == 0 and n > 3:
    print("Yes")
elif n % 5 == 0 and n > 5:
    print("Yes")
elif n % 7 == 0 and n > 7:
    print("Yes")
else:
    print("No")
