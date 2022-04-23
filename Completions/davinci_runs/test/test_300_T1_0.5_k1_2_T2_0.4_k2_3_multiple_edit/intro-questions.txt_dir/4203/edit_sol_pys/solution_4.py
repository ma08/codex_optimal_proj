
def main():
    s = input()[:-1]
    if s[0].isupper() and s[1:].islower() and s[2:].count('C') == 1:
        print('AC')
    else:
        print('WA')




if __name__ == '__main__':
    main()
