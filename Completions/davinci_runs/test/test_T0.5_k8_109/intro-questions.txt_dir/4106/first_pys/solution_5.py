
import sys

def main():
    n,k,x = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))

    # if x < k:
    #     print(-1)
    #     return

    # if k == 1:
    #     print(sum(a))
    #     return

    # # if k == 2:
    # #     print(max(a))
    # #     return

    # if k == 2:
    #     if x == 2:
    #         print(sum(a))
    #         return
    #     else:
    #         print(max(a))
    #         return

    # if k == 3:
    #     if x == 3:
    #         print(sum(a))
    #         return
    #     else:
    #         print(max(a))
    #         return

if __name__ == '__main__':
    main()