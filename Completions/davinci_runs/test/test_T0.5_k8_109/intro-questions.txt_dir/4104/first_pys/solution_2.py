

# My Solution

def calculate(expression):
    # Write your code here
    expression = expression.split('-')
    result = 0
    for i in range(len(expression)):
        if i == 0:
            result += int(expression[i])
        else:
            result -= int(expression[i])
    return result

print(calculate('8-7+6-5+4-3+2-1-0'))
print(calculate('2+2'))
print(calculate('112-37'))