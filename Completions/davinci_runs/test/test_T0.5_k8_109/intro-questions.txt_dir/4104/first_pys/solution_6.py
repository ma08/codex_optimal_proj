

def eval_expr(expr):
    a = expr.split('+')
    a = [int(i) for i in a]
    b = a[0]
    for i in a[1:]:
        b = b - i
    return b

print(eval_expr(input()))