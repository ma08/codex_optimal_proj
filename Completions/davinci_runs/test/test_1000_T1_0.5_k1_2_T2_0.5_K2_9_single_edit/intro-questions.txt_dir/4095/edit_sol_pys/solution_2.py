
def median(seq):
    return seq[len(seq)//2] if len(seq) % 2 else (seq[len(seq)//2] + seq[len(seq)//2 - 1])//2

def main():
    n, m = map(int, input().split())
    seq = list(map(int, input().split()))
    c = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            c += 1 if median(seq[i:j+1]) == m else 0
    print(c)

if __name__ == '__main__':
    main()
