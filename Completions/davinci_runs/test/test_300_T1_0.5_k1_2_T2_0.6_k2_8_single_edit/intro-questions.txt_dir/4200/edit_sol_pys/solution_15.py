

def main():
    S = input()
    T = input()
    if S == T:
        print('same')
    elif S.lower() == T.lower():
        print('case-insensitive')
    else:
        print('different')

if __name__ == '__main__':
    main()
