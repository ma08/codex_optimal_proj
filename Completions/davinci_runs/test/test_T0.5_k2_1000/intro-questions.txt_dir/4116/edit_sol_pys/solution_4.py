
N = int(input())
if N % 2 == 0 and N > 2:
    print("Yes")
elif N % 3 == 0 and N > 2:
    print("Yes")
elif N % 5 == 0 and N > 2:
    print("Yes")
elif N % 7 == 0 and N > 2:
    print("Yes")
else:
    print("No")
