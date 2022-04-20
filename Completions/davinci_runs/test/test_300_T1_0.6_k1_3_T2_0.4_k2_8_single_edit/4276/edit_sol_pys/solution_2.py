import sys

def main():
    N, T = map(int, input().split())
    ans = 'TLE'
    for i in range(N): 
        c, t = map(int, input().split()) 
        if t <= T:
            ans = min(ans, c)
    print(ans)

if __name__ == '__main__':
    main()
