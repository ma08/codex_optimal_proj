
import sys

def main():
    n = int(input())

    ans = 1
    for i in range(1, n+1):
        ans = (ans * i) % (10**9 + 7)
    print(ans)

if __name__ == '__main__':
    main()
