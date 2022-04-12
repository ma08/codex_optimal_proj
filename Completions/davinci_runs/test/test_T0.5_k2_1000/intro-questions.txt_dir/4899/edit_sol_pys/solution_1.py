

def main():
    s = input()
    if s[-1] == 'y' and s[-2] != 'a' and s[-2] != 'i' and s[-2] != 'u' and s[-2] != 'e' and s[-2] != 'o':
        print(s[:-1] + 'ies')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x':
        print(s + 'es')
    elif s[-2:] == 'ch' or s[-2:] == 'sh':
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    main()
