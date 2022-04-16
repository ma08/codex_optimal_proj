
import re

def main():
    A, B = map(int, input().split())
    S = input()
    if re.match(r'\d{3}-\d{4}', S):
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
