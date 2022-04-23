def main():
    s = input()
    if s[0] == 'A' and s[2:len(s)-1].count('C') == 1 and s[1:].islower(): # 一文字目がAで、Cが1つだけ含まれているかどうか、それ以外が小文字かどうか
        print('AC')
    else:
        print('WA')


if __name__ == '__main__':
    main()
