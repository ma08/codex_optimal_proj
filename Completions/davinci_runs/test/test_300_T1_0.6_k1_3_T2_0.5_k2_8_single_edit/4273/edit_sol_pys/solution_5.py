
def main():
    N = int(input())
    S = [input() for i in range(N)]
    chars = {'M', 'A', 'R', 'C', 'H'}
    count = 0
    for i, s in enumerate(S):
        if s[0] not in chars:
            continue
        for j, t in enumerate(S[i+1:]):
            if t[0] not in chars:
                continue
            for k, u in enumerate(S[i+j+2:]):
                if u[0] not in chars:
                    continue
                if len({s[0], t[0], u[0]}) == 3:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()
