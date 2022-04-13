
def add(a,b):

    return a + b

def mul(a,b):

    return a * b

x = int(input())
y = int(input())
op = input()  # '+' or '*'

if op == '+':  # addition
    print(add(x, y))
elif op == '*':  # multiplication
    print(mul(x, y))
