

# TODO: fix
n = int(input())

# if n is even, Alice can win by breaking a piece of length 1
if (n % 2 == 0):
    print("Alice")
    print(1)
else:
    print("Bob")
