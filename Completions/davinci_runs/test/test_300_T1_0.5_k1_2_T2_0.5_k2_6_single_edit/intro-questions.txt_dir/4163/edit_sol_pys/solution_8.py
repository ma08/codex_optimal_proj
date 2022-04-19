

def main():
    n = int(input())
    cnt_1 = 0
    cnt_2 = 0
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:
            cnt_1 += 1
            cnt_2 += 1
        else:
            cnt_1 = 0
            cnt_2 = 0
        if cnt_1 >= 3 or cnt_2 >= 3:
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
