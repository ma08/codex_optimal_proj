

# n = int(input())
# l = [int(x) for x in input().split()]

# l = [21,34,18,9]
# n = len(l)

def max_jumping(l):
    if len(l) == 1:
        return l[0]
    else:
        l = sorted(l)
        return l[-1] + max_jumping(l[:-1]) - 1


# a = int(input())
# b = int(input())

a = 21
b = 34

def max_jumping(a, b):
    if a == b:
        return a
    else:
        return max(a, b) + max_jumping(min(a, b) + 1, max(a, b) - 1)

print(max_jumping(a, b))
# print(max_jumping(l))
