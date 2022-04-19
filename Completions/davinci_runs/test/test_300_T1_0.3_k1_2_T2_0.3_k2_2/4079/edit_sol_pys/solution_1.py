
import sys

def is_diverse(s):
    return len(s) == 1 or (len(set(s)) == len(s) and ord(s[0]) + len(s) - 1 == ord(s[-1]) and all(ord(s[i]) - ord(s[i-1]) == 1 for i in range(1, len(s))))

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        s = sys.stdin.readline().strip()
        print('Yes' if is_diverse(s) else 'No')

if __name__ == '__main__':
    main()
