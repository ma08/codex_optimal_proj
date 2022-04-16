

def main():
    y, p = input().split()
    if y[-1] == 'e':
        print(y + 'x' + p, end='')
    elif y[-1] in 'aiou':
        print(y[:-1] + 'ex' + p, end='')
    else:
        print(y + p, end='')

if __name__ == "__main__":
    main()
