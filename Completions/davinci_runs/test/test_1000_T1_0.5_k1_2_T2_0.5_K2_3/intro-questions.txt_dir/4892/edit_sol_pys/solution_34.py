

import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = []
    for i in range(n):
        l = sys.stdin.readline().strip().split()
        passwords.append([l[0], float(l[1])])
    passwords.sort(key=lambda x: x[1], reverse=True)
    attempts = 0
    for p in passwords:
        attempts += 1/p[1]
    print(attempts)

if __name__ == '__main__':
    main()
