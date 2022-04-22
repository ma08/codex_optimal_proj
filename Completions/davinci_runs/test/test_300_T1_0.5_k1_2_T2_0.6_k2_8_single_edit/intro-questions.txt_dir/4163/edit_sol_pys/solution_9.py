import sys
input = sys.stdin.readline



def main():
    n = int(input().strip())
    cnt = 0
    for i in range(n):
        d1, d2 = map(int, input().split(" "))
        if d1 == d2:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
