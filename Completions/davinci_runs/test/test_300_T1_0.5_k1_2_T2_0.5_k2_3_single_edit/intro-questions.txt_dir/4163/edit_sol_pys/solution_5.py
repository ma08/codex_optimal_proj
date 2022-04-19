

def main():
    a = list(map(int, input().split()))
    n = int(input())
    cnt = 0
    for i in range(n-1):
        if a[i] == a[i+1]:
            cnt += 1
        else:
            cnt = 0
        if cnt >= 3:
            print('Yes')
            break
    else:
        print('No')

if __name__ == '__main__':
    main()
