
import sys

def main():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    a = [0] * n
    c = [0] * n
    for i in range(n):
        a[i] = ord(s[i])-ord('a')
    ans = 1
    for i in range(1,n):
        if a[i]<a[i-1]:
            ans+=1
        c[i] = ans
    print(ans)
    print(*c)


if __name__ == '__main__':
    main()
