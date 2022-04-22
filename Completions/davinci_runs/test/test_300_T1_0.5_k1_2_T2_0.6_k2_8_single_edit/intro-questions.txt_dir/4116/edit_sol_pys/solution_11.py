

N = int(input())
if N % 2 == 0 and N > 20:
    print("Not Weird")
elif N % 2 == 0 and N > 5:
    print("Weird")
elif N % 2 == 0 and N > 1:
    print("Not Weird")
elif N % 2 == 0 and N < 1:
    print("Weird")
else:
    print("No")
