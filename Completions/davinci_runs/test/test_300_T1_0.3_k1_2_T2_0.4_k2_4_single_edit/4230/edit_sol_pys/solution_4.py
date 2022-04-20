

def main():
    x, n = map(int, input().split())
    p = list(map(int, input().split()))
    ans = []
    for i in range(101):
        if i not in p:
            ans.append(i)
    ans.sort()
    print(ans[min(range(len(ans)), key=lambda i: abs(ans[i] - x))])


if __name__ == '__main__':
    main()
