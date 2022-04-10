

def main():
    n,h,l,r = map(int,input().split())
    a = list(map(int,input().split()))
    # 计算n个时间段内，经过h小时后，每个小时是否在[l,r]内
    b = [0 for _ in range(n)]
    for i in range(n):
        b[i] = [(a[i] + j) % h for j in range(h)]
    # print(b)
    # 如果第i个时间段内，经过h小时后，存在a >= l and a <=r，则该时间段是好的
    c = [0 for _ in range(n)]
    for i in range(n):
        for j in range(h):
            if b[i][j] >= l and b[i][j] <= r:
                c[i] = 1
                break
    # print(c)
    # 如果第i个时间段是好的，则可以选择在第i-1个时间段，睡i-1天，或者i天，选择最大的
    d = [0 for _ in range(n)]
    d[0] = c[0]
    d[1] = max(c[0],c[1])
    for i in range(2,n):
        d[i] = max(d[i-1],d[i-2]+c[i])
    print(d[n-1])

if __name__ == "__main__":
    main()
