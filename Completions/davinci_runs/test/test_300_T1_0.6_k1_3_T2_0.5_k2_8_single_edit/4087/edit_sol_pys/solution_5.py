

# Getting inputs
n, k = map(int, input().split())


# Printing the answer if the first condition is met else printing the 2nd condition
if n % 2 == 0:
    print(n + 2 * k)
else:
    print(n + (k - 1) * 2)
