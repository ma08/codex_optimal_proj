

def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = []
    i = 0
    j = n - 1
    while i < j:
        if a[i] < a[j]:
            ans.append(a[i])
            i += 1
        else:
            ans.append(a[j])
            j -= 1
    ans.append(a[i])
    i = 0
    j = 0
    k = 1
    res = []
    while i < len(ans):
        if i == len(ans) - 1:
            res.append(ans[i])
            break
        if ans[i] < ans[i + 1]:
            res.append(ans[i])
            i += 1
        else:
            res.append(ans[i + 1])
            i += 2
    print(len(res))
    for i in res:
        if i == a[j]:
            print("L", end="")
            j += 1
        else:
            print("R", end="")
            j += 1

if __name__ == "__main__":
    main()