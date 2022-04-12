
import sys

def main():
    n = int(sys.stdin.readline().strip())
    passwords = []
    for i in range(n):
        passwords.append(sys.stdin.readline().strip().split())
    passwords.sort(key=lambda x: float(x[1]), reverse=True)
    attempts = 0
    for p in passwords:
        attempts += 1/float(p[1])
    print(round(attempts, 1))

if __name__ == '__main__':
    main()
