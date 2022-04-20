

def median(n, m, seq):
    c = 0
    for i in range(n):
        for j in range(i, n):
            if len(seq[i:j+1]) % 2 == 0:
                med = seq[i:j+1][len(seq[i:j+1])//2] + seq[i:j+1][len(seq[i:j+1])//2 - 1]
            else:
                med = seq[i:j+1][len(seq[i:j+1])//2]
            if med == m:
                c += 1
    return c

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    print(median(n, m, seq))

if __name__ == '__main__':
    main()
