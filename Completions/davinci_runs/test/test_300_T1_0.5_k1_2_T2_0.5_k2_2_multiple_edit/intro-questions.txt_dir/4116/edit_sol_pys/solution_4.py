

N = int(input())
if N % 2 == 0 and N > 20:
    print("yes")
elif N % 3 == 0 and N > 30:
    print("yes")
elif N % 5 == 0 and N > 50:
    print("yes")
elif N % 7 == 0 and N > 70:
    print("yes")
else:
    print("No")
