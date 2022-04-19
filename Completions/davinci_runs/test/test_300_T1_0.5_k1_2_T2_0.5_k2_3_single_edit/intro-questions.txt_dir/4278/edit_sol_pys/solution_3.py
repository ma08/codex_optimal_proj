import sys
sys.setrecursionlimit(10**7)

# My code here
def main():
    a, b = input().split()
    if a[-1] == b[0] and a[0] == b[-1]:
        print('YES')
    else:
        print('NO')

if __name__ == '__main__':
    main()
