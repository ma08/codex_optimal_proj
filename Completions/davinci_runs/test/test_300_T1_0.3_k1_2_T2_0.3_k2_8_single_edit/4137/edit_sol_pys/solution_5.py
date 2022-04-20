
import re

def bf_calc(expr):
    expr = expr.replace('+', ' + ')
    expr = expr.replace('-', ' - ')
    expr = expr.replace(' ', '')
    nums = re.findall(r'\d+', expr)
    signs = re.findall(r'[+-]', expr)
    result = int(nums[0])
    for i in range(1, len(nums)):
        if signs[i-1] == '+':
            result += int(nums[i])
        else:
            result -= int(nums[i])
    return result


def bf_gen(expr):
    result = bf_calc(expr)
    output = ''
    for i in range(0, result):
        output += '+'
    output += '>'
    output += '.'
    return output

if __name__ == '__main__':
    expr = input()
    print(bf_gen(expr))
