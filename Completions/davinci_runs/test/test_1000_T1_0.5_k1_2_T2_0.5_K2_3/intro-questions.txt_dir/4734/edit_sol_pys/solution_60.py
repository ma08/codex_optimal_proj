

def main():
    x, y = input().split()
    if x[-1] == 'e':
        print(x + 'x' + y)
    elif x[-1] in 'aiou':
        print(x[:-1] + 'ex' + y)
    elif x[-2:] == 'ex':
        print(x + y)
    else:
        print(x + 'ex' + y)

main()
