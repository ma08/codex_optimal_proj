
N = int(input("Enter a number: "))
if N > 2 and N % 2 == 0:
    print("Yes")
elif N > 3 and N % 3 == 0:
    print("Yes")
elif N > 5 and N % 5 == 0:
    print("Yes")
elif N > 7 and N % 7 == 0:
    print("Yes")
else:
    print("No")
