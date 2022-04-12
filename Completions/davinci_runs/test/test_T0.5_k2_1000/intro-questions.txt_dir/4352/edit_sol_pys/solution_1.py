a, b = map(int, input().split())

def judge(a: int, b: int) -> str:
    if a == 1:
        if b == 1:
            return 'Draw'
        else:
            return 'Alice'
    elif b == 1:
        return 'Bob'
    else:
        if a > b:
            return 'Alice'
        elif a < b:
            return 'Bob'
        else:
            return 'Draw'

print(judge(a, b))
