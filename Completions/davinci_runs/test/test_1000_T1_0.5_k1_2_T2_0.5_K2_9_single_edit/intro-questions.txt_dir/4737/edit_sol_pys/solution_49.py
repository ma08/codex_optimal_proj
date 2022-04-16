

def main():
    n, p = [int(x) for x in input().split()]  # 分别表示初始的钱数和买的饮料数
    price = [int(x) for x in input().split()]  # 分别表示每种饮料的价格
    price.sort()
    if price[p] > 300:
        print("0 0")
        return
    ans = 0
    for i in range(p, n):
        if price[i] > 300:
            break
        ans += 1
    print(ans, sum(price[:ans]))

main()
