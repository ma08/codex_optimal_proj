

b, k, g = map(int, input().split())  # b is the number of books, k is the number of books in a shelf, g is the number of books in a group.

if k >= b:
    print(1)
else:
    print(b // (g - 1) + 1 if b % (g - 1) != 0 else b // (g - 1))  # if b % (g - 1) != 0, the last shelf will have less than g books
