

def cat_or_dog(a, b, x):
    return 'YES' if x <= a + b and x >= a and x <= a + b / 2 else 'NO'


A, B, X = map(int, input().split())
print(cat_or_dog(A, B, X))
