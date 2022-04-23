

def main():
    N = int(input())
    S = [input() for _ in range(N)]
    chars = ['M', 'A', 'R', 'C', 'H']
    count = 0
    for i, s1 in enumerate(S):
        for j, s2 in enumerate(S[i+1:], i+1):
            for k, s3 in enumerate(S[j+1:], j+1):
                if s1[0] in chars and s2[0] in chars and s3[0] in chars:
                    if len(set([s1[0], s2[0], s3[0]])) == 3:
                        count += 1  # s1, s2, s3を使う場合の数
    print(count)

if __name__ == '__main__':
    main()
