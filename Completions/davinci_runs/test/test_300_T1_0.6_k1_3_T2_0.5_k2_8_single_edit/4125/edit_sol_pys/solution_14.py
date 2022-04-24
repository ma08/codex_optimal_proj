

def main():
    n, k = map(int, input().split())
    p_list = list(map(int, input().split()))
    p_list.sort()
    ans = 0
    for i in range(k):
        ans += p_list[i]
    print(ans)

if __name__ == '__main__':
    main()
