

def main():
    L, H = map(int, input().split()) # L = 下限、H = 上限
    ans = 0
    for i in range(L, H + 1, 2):
        if len(set(str(i))) == 3 and i % 5 != 0: # i % 5 != 0 の条件を付け加えた
            ans += 1
    print(ans)

main()
