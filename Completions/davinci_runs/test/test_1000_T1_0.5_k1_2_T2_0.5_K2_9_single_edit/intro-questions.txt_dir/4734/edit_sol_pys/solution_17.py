

def main():
    Y, P = input().split()
    if Y[-1] == 'e':
        print(Y + 'x' + P[1:])
    elif Y[-1] in 'aiou':
        print(Y[:-1] + 'ex' + P[1:])
    elif Y[-2:] == 'ex':
        print(Y + P[1:])
    else:
        print(Y + 'ex' + P[1:])

main()
