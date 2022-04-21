

num = int(input())
if num % 2 == 0 and num > 2:
    print("Yes")
elif num % 3 == 0 and num > 3:
    print("Yes")
elif num % 5 == 0 and num > 5:
    print("Yes")
elif num % 7 == 0 and num > 7:
    print("Yes")
else:
    print("No")
