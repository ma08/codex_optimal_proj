

n = int(input())
if n == 1:
    print("NO")
elif n > 1:
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print("YES")
    else:
        print("NO")
