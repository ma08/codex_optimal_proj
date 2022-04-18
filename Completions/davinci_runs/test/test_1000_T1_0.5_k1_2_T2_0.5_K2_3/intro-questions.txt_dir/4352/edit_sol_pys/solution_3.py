a = int(input())
b = int(input())



def judge(a=1, b=1):
    if a == 1 or b == 1:
        return 'Alice' if a == 1 else 'Bob'

    if a > b:
        return 'Alice'
    elif a < b:
        return 'Bob'
    else:
        return 'Draw'

print(judge(a, b))
