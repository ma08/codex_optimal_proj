

n = int(input())

if n % 2 == 0 and 2 <= n <= 5:
    print("Even")
elif n % 2 == 1 and 6 <= n <= 20:
elif n % 2 == 0 and 20 <= n:
    print("Even")
elif n % 2 == 1 and n > 20:
    print("Odd")

    print("Odd")
else:
    print("Either")
