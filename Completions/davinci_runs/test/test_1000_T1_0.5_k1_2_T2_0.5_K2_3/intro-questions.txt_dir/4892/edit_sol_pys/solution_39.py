

import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = []
    for i in range(n):
        passwords.append(sys.stdin.readline().strip().split())
    passwords.sort(key=lambda x: float(x[1]), reverse=True)
    # print(passwords) 
    attempts = 0
    for i in range(len(passwords)):
        attempts += 1/float(passwords[i][1])
    print(attempts)

if __name__ == '__main__':
    main()
