
import sys

def isValid(password):
    has_digit = False
    for l in password:
        if l.isdigit():
            has_digit = True
    if len(password) >= 10 and has_digit:
        return True
    else:
        return False

def main():
    n = int(sys.stdin.readline())
    passwords = [sys.stdin.readline().strip() for _ in range(n)]
    valid = 0
    for p in passwords:
        if isValid(p):
            valid += 1
    print(valid)

if __name__ == '__main__':
    main()
