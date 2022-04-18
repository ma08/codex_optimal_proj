

def cat_or_dog(a, b, x):
    if x <= a + b and x >= a and x <= a + b / 2:
        return 'YES'
    else:
        return 'NO'

A, B, X = map(int, input().split())
print(cat_or_dog(A, B, X))
