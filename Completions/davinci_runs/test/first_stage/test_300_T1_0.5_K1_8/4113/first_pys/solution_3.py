

N = int(input())

if N % 4 == 0 or N % 7 == 0 or N % 11 == 0 or N == 4 or N == 7 or N == 11:
    print("Yes")
elif N >= 8 and N % 4 == 3 and (N - 8) % 7 == 0:
    print("Yes")
elif N >= 5 and N % 7 == 3 and (N - 5) % 4 == 0:
    print("Yes")
else:
    print("No")