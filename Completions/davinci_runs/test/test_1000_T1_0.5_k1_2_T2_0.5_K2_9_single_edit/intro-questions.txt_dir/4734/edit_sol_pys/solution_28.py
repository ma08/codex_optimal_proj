

def main():
    Y, P = input().split()
    if Y[-1] == 'e' and Y[-2] not in 'aiou':
        print(Y + 'x' + P)
    elif Y[-1] in 'aiou':
        print(Y[:-1] + 'ex' + P)
    elif Y[-2:] == 'ex' and Y[-3] not in 'aiou':
        print(Y + P)
    else:
        print(Y + 'ex' + P)

main()
