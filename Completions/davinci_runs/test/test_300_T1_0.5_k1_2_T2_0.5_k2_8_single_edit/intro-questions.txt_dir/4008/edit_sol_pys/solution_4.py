
def main():
    n, k = map(int, input().split())  # n, k = (int(x) for x in input().split())
    a = list(map(int, input().split()))  # a = [int(x) for x in input().split()]
    d = {}  # d = collections.Counter(a)
    for i in range(n):  # for i in a:
        if a[i] in d:  # if i in d:
            d[a[i]] += 1  # d[i] += 1
        else:
            d[a[i]] = 1  # d[i] = 1
    if len(d) > k:  # if len(d) > k:
        print("NO")
        return  # return
    ans = [0] * n  # ans = [0] * n
    cnt = 1  # cnt = 1
    for i in range(n):  # for i in range(n):
        if a[i] in d:  # if a[i] in d:
            ans[i] = cnt  # ans[i] = cnt
            d[a[i]] -= 1  # d[a[i]] -= 1
            if d[a[i]] == 0:  # if d[a[i]] == 0:
                cnt += 1  # cnt += 1
            if cnt > k:  # if cnt > k:
                print("NO")
                return  # return
    print("YES")  # print("YES")
    print(' '.join(map(str, ans)))  # print(' '.join(map(str, ans)))



if __name__ == '__main__':  # if __name__ == "__main__":
    main()  # main()
