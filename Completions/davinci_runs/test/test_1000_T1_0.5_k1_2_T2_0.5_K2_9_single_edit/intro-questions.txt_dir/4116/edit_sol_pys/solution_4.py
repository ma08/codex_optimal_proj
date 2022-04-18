

N = int(input())
if N % 2 == 0 and N > 2 and N != 6:
    print("Yes")
elif N % 3 == 0 and N > 3 and N != 9:
    print("Yes")
elif N % 5 == 0 and N > 5 and N != 10:
    print("Yes")
elif N % 7 == 0 and N > 7:
    print("Yes")
else:
    print("No")
