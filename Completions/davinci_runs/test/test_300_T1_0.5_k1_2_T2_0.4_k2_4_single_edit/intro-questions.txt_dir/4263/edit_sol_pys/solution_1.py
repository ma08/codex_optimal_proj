
import sys

def main():
    s = sys.stdin.readline().rstrip()
    ans = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            if s[i:j+1].count('A') + s[i:j+1].count('C') + s[i:j+1].count('G') + s[i:j+1].count('T') == j-i+1:
                ans = max(ans, j-i+1)
    print(ans)

if __name__ == '__main__':
    main()
