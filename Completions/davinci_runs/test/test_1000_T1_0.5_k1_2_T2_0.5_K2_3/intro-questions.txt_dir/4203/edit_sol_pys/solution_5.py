
def main():
    s = input()
    if s[0] == 'A' and s[2:len(s) - 1].count('C') == 1 and s[1:].islower() and s[0:].count('A') == 1:
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
