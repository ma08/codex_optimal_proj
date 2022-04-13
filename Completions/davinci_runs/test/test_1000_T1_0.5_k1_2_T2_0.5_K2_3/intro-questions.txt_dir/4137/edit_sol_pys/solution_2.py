

import re

def brainfuck(expr):
    expr = re.sub(r'([0-9]+)([+-])', r'\1 \2', expr)
    expr = re.sub(r'([+-])([0-9]+)', r'\1 \2', expr)
    expr = re.sub(r'([0-9]+)([+-])([0-9]+)', r'\1 \2 \3', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12 \13 \14', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12 \13 \14 \15 \16', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12 \13 \14 \15 \16 \17 \18', expr)
    expr = re.sub(r'([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)([+-])([0-9]+)', r'\1 \2 \3 \4 \5 \6 \7 \8 \9 \10 \11 \12 \13 \14 \15 \16 \17 \18 \19 \20', expr)
    expr = expr.split()
    result = 0
    for i in range(0, len(expr), 2):
        if expr[i] == '+':
            result += int(expr[i+1])
        else:
            result -= int(expr[i+1])
    expr = ' ' + expr[0] # add spaces between operators and numbers
    for i in range(1, len(expr), 2):
        expr = expr[:i] + ' ' + expr[i] + ' '
    while '  ' in expr: # remove extra spaces (if any)
        expr = expr.replace('  ', ' ') 
    expr = expr.split()
    result_bf = ''
    for i in range(len(expr)):
        if expr[i] == '+':
            result_bf += '+'
        elif expr[i] == '-':
            result_bf += '-'
        else:
            result_bf += '>'
    result_bf += '>' # move pointer to last cell
    result_bf += '<' * len(expr)
    result_bf += '[' # start loop
    for i in range(len(expr)):
        if expr[i] == '+':
            result_bf += '<+>'
        elif expr[i] == '-':
            result_bf += '<->'
    result_bf += '-]<'
    result_bf += '+' * result
    result_bf += '.'
    return result_bf

def main():
    expr = input()
    print(brainfuck(expr))

if __name__ == '__main__':
    main()
