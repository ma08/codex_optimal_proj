import sys
import math

def main():
    n = int(sys.stdin.readline().strip()) # number of passwords
    passwords = []
    for i in range(n):
        line = sys.stdin.readline().strip()
        passwords.append(line.split()) # [password, value]
    passwords.sort(key=lambda x: float(x[1]), reverse=True) # sort by value
    total = 0
    for i in range(len(passwords)):
        total += (i+1) * float(passwords[i][1]) # index * value
    print(total)

if __name__ == '__main__':
    main()
