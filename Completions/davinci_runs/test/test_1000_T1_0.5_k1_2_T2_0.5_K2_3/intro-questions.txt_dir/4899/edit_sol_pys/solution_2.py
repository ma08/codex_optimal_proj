

def main():
    s = input()
    if s[-1] == 'y':
        print(s[:-1] + 'ies', end='')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x':
        print(s + 'es', end='')
    else:
        print(s + 's', end='')

if __name__ == '__main__':
    main()
