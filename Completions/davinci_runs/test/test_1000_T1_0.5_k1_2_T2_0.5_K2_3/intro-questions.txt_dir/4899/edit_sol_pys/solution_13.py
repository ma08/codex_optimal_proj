

def main():
    s = input()
    if s[-2:] == 'ch' or s[-2:] == 'sh':
        print(s + 'es')
    elif s[-1] == 'f':
        print(s[:-1] + 'ves')
    elif s[-1] == 'y' and s[-2] not in 'aeiou':
        print(s[:-1] + 'ies') 
    else:
        print(s)

if __name__ == '__main__':
    main()
