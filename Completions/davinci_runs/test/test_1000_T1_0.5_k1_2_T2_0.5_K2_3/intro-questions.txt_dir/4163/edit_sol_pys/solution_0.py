

def main():
    n = int(input())
    cnt = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a == b:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            return
            print("Yes")
            break
    else:
        print("No")

if __name__ == '__main__':
    main()
