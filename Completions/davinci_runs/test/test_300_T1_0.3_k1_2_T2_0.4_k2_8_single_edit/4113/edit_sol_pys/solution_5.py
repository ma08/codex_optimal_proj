
N = int(input())

if N == 4 or N == 7:
    print("YES")
elif N % 4 == 0 or N % 7 == 0:
    print("YES")
elif N % 11 == 0 or N == 11:
    print("YES")
else:
    print("NO")
