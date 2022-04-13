

import sys

    # n = int(input()) 
def main():
    n = int(sys.stdin.readline().strip())
    passwords = []
        # passwords.append(input().split())
    for i in range(n):
        passwords.append(sys.stdin.readline().strip().split())
    passwords.sort(key=lambda x: float(x[1]), reverse=True)
    # print(passwords)
    attempts = 0.0
    for p in passwords:
        attempts += 1.0/float(p[1])
    print(attempts)

if __name__ == '__main__':
    main()
