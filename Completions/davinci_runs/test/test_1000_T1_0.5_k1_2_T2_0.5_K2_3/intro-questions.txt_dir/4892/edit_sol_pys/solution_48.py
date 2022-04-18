

import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = {}
    for i in range(n):
        l = sys.stdin.readline().strip().split()
        passwords[float(l[1])] = l[0]
    passwords.sort(key=lambda x: float(x[1]))
    print(passwords)
    attempts = 0
    for p in passwords:
        attempts += 1 / p
        print(passwords[p])
    print(attempts)

if __name__ == '__main__':
    main()
