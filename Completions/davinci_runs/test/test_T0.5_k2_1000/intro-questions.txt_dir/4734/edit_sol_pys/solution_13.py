

def main():
    y, p = input().split() 
    if y.endswith(('ex', 'ix')):
        print(y + p)
    elif y.endswith(('e', 'i')):
        print(y[:-1] + 'x' + p)
    elif y.endswith(('a', 'i', 'o', 'u')):
        print(y[:-1] + 'ex' + p)
    else:
        print(y + 'ex' + p)

if __name__ == "__main__":
    main()
