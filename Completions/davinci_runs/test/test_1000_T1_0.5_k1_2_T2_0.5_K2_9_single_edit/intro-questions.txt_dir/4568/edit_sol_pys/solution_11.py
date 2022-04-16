from itertools import combinations


N, M = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(M)]

def main():
    # s_list = [s for s in S]
    # print(s_list)
    # print(s_list[:3])
    # print(s_list[3:])
    # print(set(s_list[:3]))
    # print(set(s_list[3:]))
    # print(set(s_list[:3]) & set(s_list[3:]))
    # print(len(set(s_list[:3]) & set(s_list[3:])))
    # print(set(s_list[:4]) & set(s_list[4:]))
    # print(len(set(s_list[:4]) & set(s_list[4:])))
    ans = 0
    for i in range(1, N):
        ans = max(ans, len(set(S[:i]) & set(S[i:])))
    print(ans)

if __name__ == '__main__':
    main()
