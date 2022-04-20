

def main():
    n = int(input())
    a_list = list(map(int, input().split()))
    a_list.sort()
    b_list = list(map(int, input().split()))
    b_list.sort()
    c_list = list(map(int, input().split()))
    c_list.sort()
    a_i = 0
    b_i = 0
    c_i = 0
    ans = 0
    while b_i < n:
        while a_i < n and a_list[a_i] < b_list[b_i]:
            a_i += 1
        while c_i < n and c_list[c_i] <= b_list[b_i]:
            c_i += 1
        ans += a_i * (n - c_i)
        b_i += 1
    print(ans)

if __name__ == '__main__':
    main()
