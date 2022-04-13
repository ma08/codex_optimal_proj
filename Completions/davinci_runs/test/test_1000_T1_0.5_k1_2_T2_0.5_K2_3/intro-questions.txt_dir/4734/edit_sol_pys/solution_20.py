

def main():
    X, Y = input().split()
    if X[-1] == 'e' and Y[0] == 'x':
        print(X + 'x' + Y)
    elif X[-1] in 'aiou' and Y[0] == 'x':
        print(X[:-1] + 'ex' + Y)
    elif X[-2:] == 'ex' and Y[0] == 'x':
        print(X + Y)
    elif Y[0] == 'x':
        print(X + 'ex' + Y)

main()
