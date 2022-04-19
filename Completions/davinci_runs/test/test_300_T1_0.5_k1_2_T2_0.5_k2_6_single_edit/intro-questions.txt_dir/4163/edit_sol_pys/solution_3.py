
def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        d_1, d_2 = map(int, input().split())
        if d_1 == d_2:
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
