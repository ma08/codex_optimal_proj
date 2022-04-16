

def main():
    Y, P = input().split()
    if Y[-1] == 'e':
        print(Y + 'x' + P)
    elif Y[-1] in 'aiou' and Y[-2] not in 'aeiou':
        print(Y[:-1] + 'ex' + P)
    elif Y[-2:] == 'ex':
        print(Y + P)
    else:
        print(Y + 'ex' + P)

main()
