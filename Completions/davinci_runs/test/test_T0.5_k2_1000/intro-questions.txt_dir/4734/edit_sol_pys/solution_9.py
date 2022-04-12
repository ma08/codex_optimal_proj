

def main():
    s, p = input().split(' ')
    if s[-1] == 'e':
        print(s + 'x' + p)
    elif s[-1] in 'aiou':
        print(s[:-1] + 'ex' + p)
    else:
        print(s + p)

if __name__ == "__main__":
    main()
