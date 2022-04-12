

def main():
    s = input()
    if s[-1] == 'y':
        print(s[:-1] + 'ies')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x' or s[-1] == 'h':
        print(s + 'es')
    elif s[-2:] == 'ch' or s[-2:] == 'sh':
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    main()
