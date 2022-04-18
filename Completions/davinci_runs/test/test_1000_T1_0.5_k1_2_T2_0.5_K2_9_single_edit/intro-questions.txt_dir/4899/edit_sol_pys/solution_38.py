

def main():
    s = input()
    if s[-1] == 'y' and len(s) > 1:
        print(s[:-1] + 'ies')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x' or s[-1] == 'z':
        print(s + 'es')
    elif s[-2:] == 'ch' or s[-2:] == 'sh':
        print(s + 'es')
    elif s[-1] == 'f' or s[-2:] == 'fe':
        print(s[:-1] + 'ves')
    else:
        print(s)

if __name__ == '__main__':
    main()
