
a, b = map(int, input().split()) # 入力

def judge(a, b): # 判定
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
