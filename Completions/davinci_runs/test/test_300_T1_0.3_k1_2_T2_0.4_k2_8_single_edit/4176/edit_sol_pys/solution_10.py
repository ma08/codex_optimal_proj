
def main():
    a, b = map(int, input().split())
    if a > b:
        a, b = b, a
    ans = a
    while ans % b != 0:  # 注意这里不能用if，因为if只会执行一次，while会一直循环
        ans += a
    print(ans)

if __name__ == '__main__':
    main()
