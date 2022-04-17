
def main():
    n = int(input())
    cnt = 1
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2 and cnt >= 3:
            print("Yes")
            break
        elif d1 == d2:
            cnt += 1
        else:
            cnt = 0
    else:
        print("No")

if __name__ == '__main__':
    main()
