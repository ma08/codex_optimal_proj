

import re

def bf_calc(expr):
    print(expr)
    expr = expr.replace('+', ' + ')
    expr = expr.replace('-', ' - ')
    expr = expr.replace(' ', '')
    print(expr)
    nums = re.findall(r'\d+', expr)
    print(nums)
    signs = re.findall(r'[+-]', expr)
    print(signs)
    result = int(nums[0])
    for i in range(1, len(nums)):
        if signs[i-1] == '+':
            result += int(nums[i])
        else:
            result -= int(nums[i])
    print(result)
    return result


def bf_gen(expr):
    result = bf_calc(expr)
    print(result)
    output = ''
    for i in range(0, result):
        output += '+'
    output += '>'
    output += '.'
    return output

if __name__ == '__main__':
    expr = input()
    print(bf_gen(expr))
