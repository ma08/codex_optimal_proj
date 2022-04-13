
def add(a,b):
    return a + b

def mul(a,b):
    return a * b

x = int(input())
y = int(input())
op = input() # '+' or '*'

if op == '+':  # Addition
    print(add(x,y))
elif op == '*':  # Multiplication
    print(mul(x,y))
