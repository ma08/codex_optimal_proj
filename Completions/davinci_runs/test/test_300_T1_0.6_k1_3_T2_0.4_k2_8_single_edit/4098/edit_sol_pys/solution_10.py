

def solve(n, k, a):
    a.sort()
    a.append(a[-1] + 5)  # 下限を決める
    #print(a)
    cnt = 0
    for i in range(n):
        if i == 0 or a[i] - a[i-1] > 5:  # 初めか、前のものと5以上離れているか
            cnt += 1
            if cnt == k + 1:
                return i
    return n

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))
