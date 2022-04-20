

def main():
    n, m = map(int, input().split())
    s = input()
    t = input().split()
    s = s.split()
    print(s)
    print(t)
    # moves = []
    # for i in range(n):
    #     if s[i] != t[i]:
    #         for j in range(i+1, n):
    #             if s[j] == t[i]:
    #                 moves.append(j)
    #                 s = s[:j] + s[j+1] + s[j] + s[j+2:]
    #                 break
    # if s == t:
    #     print(len(moves))
    #     print(' '.join(map(str, moves)))
    # else:
    #     print(-1)

if __name__ == '__main__':
    main()
