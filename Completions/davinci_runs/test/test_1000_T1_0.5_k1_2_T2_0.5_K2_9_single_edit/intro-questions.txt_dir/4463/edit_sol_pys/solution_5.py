

def main():
    s = input()
    t = input()
    if ''.join(sorted(s)) < ''.join(sorted(t)):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
