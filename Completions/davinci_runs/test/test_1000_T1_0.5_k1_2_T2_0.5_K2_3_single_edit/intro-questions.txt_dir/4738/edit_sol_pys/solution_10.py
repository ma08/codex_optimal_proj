
import sys

def get_k(s):
    for k in range(1, len(s) + 1):
        if len(s) % k == 0:
            for i in range(k, len(s), k):
                if s[i:i+k] != s[i-k:i][-1] + s[i-k:i][:-1]:
                    break
            else:
                return k
    return len(s)

def main():
    s = sys.stdin.readline().strip()
    print(get_k(s))

if __name__ == '__main__':
    main()
