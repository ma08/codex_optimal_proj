

def main():
    s = raw_input()
    if s[-1] == 'y':
        print(s[:-1] + 'ies')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x':
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    main()
