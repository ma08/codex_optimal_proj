

def main():
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        a[i].sort()
    print(a)
    # for i in range(n):
    #     a[i].sort()
    # print(a)
    # for i in range(n):
    #     if a[i][0] == i+1 and a[i][1] == i+1:
    #         print(i+1)
    #         break
    # else:
    #     print(-1)

if __name__ == '__main__':
    main()