

def main():
    y, p = input().split()
    if y[-1] == 'x':
        print(y + p)
    elif y[-1] in 'aiou':
        print(y[:-1] + 'ex' + p)
    elif y[-2:] == 'ex':
        print(y + p)
    else:
        print(y + 'ex' + p)

main()
