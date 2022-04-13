

a, b, x = map(int, input().split())

def judge(a, b, x):
    if a + b >= x and a <= x and b <= x:
        return 'YES'
    else:
        return 'NO'

print(judge(a, b, x))
