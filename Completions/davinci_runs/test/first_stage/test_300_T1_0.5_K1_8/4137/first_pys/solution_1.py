

def bf_calc():
    expr = list(input())
    stack = []
    result = []
    for char in expr:
        if char.isdigit():
            stack.append(int(char))
        elif char == '+':
            result.append(sum(stack))
            stack = []
        else:
            result.append(stack[0] - stack[1])
            stack = []
    result = result[0]
    bf = ''
    while result > 0:
        bf += '+'
        result -= 1
    bf += '>++++++++++++++++++++++++++++++++++++++++++++++++.<'
    print(bf)

bf_calc()