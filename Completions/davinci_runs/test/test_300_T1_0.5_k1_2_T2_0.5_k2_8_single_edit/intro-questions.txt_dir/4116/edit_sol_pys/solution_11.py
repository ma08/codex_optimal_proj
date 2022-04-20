

N = int(input())
if N % 2 == 0 and N > 2 or N % 3 == 0 and N > 3 or N % 5 == 0 and N > 5 or N % 7 == 0 and N > 7:
    print("Yes")

else:
    print("No")
