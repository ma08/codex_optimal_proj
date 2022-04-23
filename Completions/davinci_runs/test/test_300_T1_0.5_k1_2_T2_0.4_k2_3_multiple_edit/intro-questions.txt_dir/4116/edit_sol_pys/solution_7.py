

N = int(input())
if N % 2 == 0 and N > 2:
    print("YES")
elif N % 3 == 0 and N > 3:
    print("YES")
elif N % 5 == 0 and N > 5:
    print("YES")
elif N % 7 == 0 and N > 7:
    print("YES")
else:
    print("NO")
