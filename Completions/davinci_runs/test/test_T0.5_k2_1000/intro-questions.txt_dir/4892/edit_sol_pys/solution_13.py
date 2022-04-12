
import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = []
    for i in range(n):
        passwords.append(sys.stdin.readline().strip().split())
    passwords.sort(key=lambda x: int(x[1]), reverse=True)
    attempts = 0
    for p in passwords:
        attempts += 1/int(p[1])
    print(attempts)

if __name__ == '__main__':
    main()
