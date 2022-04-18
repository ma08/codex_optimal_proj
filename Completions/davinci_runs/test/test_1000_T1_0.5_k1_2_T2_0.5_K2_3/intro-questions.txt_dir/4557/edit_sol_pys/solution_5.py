

def cat_or_dog(A, B, x):
    if x <= A + B and x >= A and x <= A + B/2:
        return 'YES'
    else:
        return 'NO'

A, B, X = map(int, input().split())
print(cat_or_dog(A, B, X))
