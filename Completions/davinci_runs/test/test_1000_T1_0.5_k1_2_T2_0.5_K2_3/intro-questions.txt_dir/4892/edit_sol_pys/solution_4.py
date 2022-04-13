

import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = {}
    for i in range(n):
        l = sys.stdin.readline().strip().split()
        passwords[float(l[1])] = l[0]
    attempts = 0
    for key in sorted(passwords.keys(), reverse=True):
        attempts += 1/key
    print(attempts)

if __name__ == '__main__':
    main()
