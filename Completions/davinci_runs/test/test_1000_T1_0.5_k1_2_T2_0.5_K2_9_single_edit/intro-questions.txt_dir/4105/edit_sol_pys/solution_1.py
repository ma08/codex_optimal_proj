

def get_digits(num):
    return [int(i) for i in str(num)]

def is_even(num):
    digits = get_digits(num)
    for i in digits:
        if i%2 != 0:
            return False
    return True

def count(n, k):
    if is_even(n) == False:
        return "NO"
    else:
        return "YES"

n, k = map(int, input().split())
print(count(n, k))
