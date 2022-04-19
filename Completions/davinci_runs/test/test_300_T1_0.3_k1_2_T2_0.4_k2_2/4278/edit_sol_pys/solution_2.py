
import sys

def main():
    n = int(sys.stdin.readline())
    s = []
    for i in range(n):
        s.append(sys.stdin.readline().rstrip())
    s.sort(key=len)
    ans = 0
    for i in range(n-1):
        for j in range(i+1, n):
            if len(s[i]) == len(s[j]) and len(s[i]) != len(set(s[i])) and len(s[j]) != len(set(s[j])):
                if sorted(s[i]) == sorted(s[j]):
                    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
