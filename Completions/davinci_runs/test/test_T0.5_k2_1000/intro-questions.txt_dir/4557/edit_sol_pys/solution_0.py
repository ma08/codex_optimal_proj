

def cat_or_dog(a, b, x): 
    if x <= a + b and x >= a and x <= a + b/2:
        return 'YES'
    else:
        return 'NO'

a, b, x = map(int, input().split())
print(cat_or_dog(a, b, x))
