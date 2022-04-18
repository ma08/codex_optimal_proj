

def cat_or_dog(A, B, X):
    if X <= A + B and X >= A and X <= A + B / 2:
        return 'YES'
    else:
        return 'NO'

A, B, X = map(int, input().split())
print(cat_or_dog(A, B, X))
