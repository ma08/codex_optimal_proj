

# ==========
# Solution 1
# ==========

a, b = list(map(int, input().split())) # split the input into 2 variables

if a > b: # if a is greater than b
    a, b = b, a # swap a and b

print(a)

# ==========
# Solution 2
# ==========

a, b = list(map(int, input().split()))

if a > b:
    a, b = b, a

print(a)
