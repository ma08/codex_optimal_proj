

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            a = a_list[i]
            b = a_list[j]
            ans = max(ans, (a*b-1)//(a+b))
    print(ans)

if __name__ == '__main__':
    main()