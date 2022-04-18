import sys,math

def main():
    # input = sys.stdin.readline
    # N = int(input())
    # P = [int(i) for i in input().split()]
    # ans = 0
    # for i in range(0, N):
    #     if P[i] == i + 1:
    #         ans += 1
    # print(ans)
    n,a,b = map(int,input().split())
    print(math.ceil(n/(a+b))*a)

if __name__ == '__main__':
    main()
