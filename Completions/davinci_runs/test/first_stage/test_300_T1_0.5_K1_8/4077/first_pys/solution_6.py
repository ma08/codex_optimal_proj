

def main():
    n,m = map(int, input().split())
    a = list(map(int, input().split()))
    s = 0
    for i in range(n):
        for j in range(i,n):
            if (j-i+1)%2 == 0:
                if a[(j+i)//2] == m:
                    s += 1
            else:
                if a[(j+i)//2] == m or a[(j+i)//2+1] == m:
                    s += 1
    print(s)

if __name__ == '__main__':
    main()