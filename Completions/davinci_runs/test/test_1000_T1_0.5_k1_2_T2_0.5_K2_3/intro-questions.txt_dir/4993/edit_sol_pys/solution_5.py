import sys

def main():
    n, m = map(int, input().split())
    parts = []
    for i in range(m):
        parts.append(input())
        if len(set(parts)) == n:
            print(i+1)
            return
    print('paradox avoided')

if __name__ == '__main__':
    main()
