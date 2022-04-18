import sys

def main():
    s = sys.stdin.readline()
    if s[-1] == 'y':
        print(s[:-1] + 'ies')
    elif s[-1] == 'o' or s[-1] == 's' or s[-1] == 'x':
        print(s + 'es')
    elif s[-2:] == 'ch':
        print(s + 'es')
    elif s[-2:] == 'sh':
        print(s + 'es')
    else:
        print(s + 's')

if __name__ == '__main__':
    main()
