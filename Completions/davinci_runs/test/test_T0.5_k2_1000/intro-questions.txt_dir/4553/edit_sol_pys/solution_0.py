
import re

def main():
    S = input()
    if re.match(r'[a-zA-Z]{1}[a-zA-Z0-9_]*', S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
