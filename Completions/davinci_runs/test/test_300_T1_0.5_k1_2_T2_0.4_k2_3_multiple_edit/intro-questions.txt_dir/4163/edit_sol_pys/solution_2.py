

def main():
    n = int(input())
    cnt = 0  # counter
    for i in range(n):
        d1, d2 = map(int, input().split())
        if d1 == d2:  # if the numbers are the same, increase counter
            cnt += 1
            # if the numbers aren't the same, reset counter
        else:
        # if the counter is greater than or equal to 3
            cnt = 0
            # print yes and break
        if cnt >= 3:
            print("Yes")
            break
        # if the counter never gets to 3, print no
    else:
        print("No")

if __name__ == '__main__':
    main()
