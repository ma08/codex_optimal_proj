

def main():
    y, p = input().split()
    if y[-1] == 'e':
        print(y + 'ex' + ' ' + p)
    elif y[-1] in 'aiou':
        print(y[:-1] + 'ex' + ' ' + p)
    else:
        print(y + ' ' + p)

if __name__ == "__main__":
    main()
