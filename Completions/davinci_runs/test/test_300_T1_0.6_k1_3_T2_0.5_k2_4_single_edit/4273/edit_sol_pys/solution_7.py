

def main():
    N = int(input())
    S = [input() for i in range(N)]
    chars = set(['M', 'A', 'R', 'C', 'H'])
    count = 0
    for i in range(N):
        for j in range(i+1, N):
            for k in range(j+1, N):
                if len(set([S[i][0], S[j][0], S[k][0]]) & chars) == 3:
                    count += 1
    print(count)

if __name__ == '__main__':
    main()
