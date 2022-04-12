
n = int(input())

if n % 2 == 0:
    print("Alice")
    print(n // 2)
else:
    print(n // 2 + 1)  # or print(n // 2 + 2)
    print("Bob")
