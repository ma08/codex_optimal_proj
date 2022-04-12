
import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = [sys.stdin.readline().strip().split() for i in range(n)]
    passwords.sort(key=lambda x: float(x[1]))
    attempts = 0
    for p in passwords:
        attempts += 1/float(p[1])
    print(attempts)

if __name__ == '__main__':
    main()
