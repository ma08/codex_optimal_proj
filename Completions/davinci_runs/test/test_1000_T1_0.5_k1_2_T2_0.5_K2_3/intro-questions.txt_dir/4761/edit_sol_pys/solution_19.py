
def main():
    L, H = map(int, input().split())
    ans = 0
    for i in range(L, H + 1, 2):
        if len(set(str(i))) == 3 and i % 5 != 0:
            ans += 1
    print(ans)

main()
