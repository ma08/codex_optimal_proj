
import sys

def main():
    with open('input.txt') as f:
        n = int(f.readline())
        a = [int(i) for i in f.readline().split()]
        s = [0 for i in range(n + 1)]
        s[0] = a[0]
        for i in range(1, n):
            s[i] = s[i - 1] + a[i]
        ans = 0    
        for i in range(n):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    ans += 1
        with open('output.txt', 'w') as f:
            f.write(str(ans))

if __name__ == '__main__':
    main()
