

def main():
    n = int(input())
    cnt = 1
    for i in range(n):
        d1, d2 = map(int, input().split())
        cnt += (d1 == d2)
        cnt = 0 if d1 != d2 else cnt
        if cnt >= 3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
