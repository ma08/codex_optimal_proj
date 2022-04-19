


def main():
    s = input()
    if s[0] == 'A' and s[2:len(s)-1].count('C') == 1 and s[1:].islower() == True:
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
