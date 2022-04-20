# My code here
def main():
    N = int(input())
    s_list = []
    for _ in range(N):
        s = input()
        s_list.append(s)
    s_sort_list = []
    for s in s_list:
        s_sort_list.append(''.join(sorted(s)))
    from collections import Counter
    c = Counter(s_sort_list)
    ans = 0
        ans += c * (c - 1) // 2
    print(ans)
    

if __name__ == '__main__':
    main()
