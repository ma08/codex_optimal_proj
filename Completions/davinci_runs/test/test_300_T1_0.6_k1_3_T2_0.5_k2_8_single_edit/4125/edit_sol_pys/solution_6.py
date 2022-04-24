

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0
    for i in range(n - 1):
        ans += a_list[i]
        if a_list[i + 1] == 0:
            a_list[i + 1] += ans
            ans = 0
    print(sum(a_list))

if __name__ == '__main__':
    main()
