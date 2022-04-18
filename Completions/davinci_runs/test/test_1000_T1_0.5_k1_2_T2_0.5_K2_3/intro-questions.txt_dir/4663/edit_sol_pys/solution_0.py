import re

def is_valid_number(number):
    if re.match(r'[789]\d{9}$', number):
        return True
    return False

if __name__ == '__main__':
    N = int(input())

    for _ in range(N):
        number = input()
        if is_valid_number(number):
            print('YES')
        else:
            print('NO')
