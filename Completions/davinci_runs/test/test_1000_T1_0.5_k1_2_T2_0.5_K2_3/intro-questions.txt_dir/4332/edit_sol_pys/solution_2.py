
n = int(input())

if n % sum([int(x) for x in list(str(n))]) == 0:
    print("Yes")
else:
    print("No")
