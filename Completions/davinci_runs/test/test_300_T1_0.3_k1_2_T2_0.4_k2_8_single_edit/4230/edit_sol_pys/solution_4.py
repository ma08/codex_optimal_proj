

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(101):
        if i not in p:
            ans.append(i)
    ans.sort()
    print(ans[min(range(len(ans)), key=lambda i: abs(ans[i]-x))])  # key=lambda i: abs(ans[i]-x) は辞書式順序のソートのキーを指定するためのもの

if __name__ == '__main__':
    main()
