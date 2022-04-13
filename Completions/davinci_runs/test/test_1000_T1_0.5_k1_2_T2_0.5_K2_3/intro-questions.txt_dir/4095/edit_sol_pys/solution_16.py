

def median(seq, n):
    seq.sort()
    if n % 2 == 0:
        return (seq[n//2] + seq[n//2 - 1])/2
    return seq[n//2]

def main():
    n, m = map(int, input().split())
    seq = map(int, input().split())
    count = 0
    for i in range(n):
        for j in range(i, n):
            if median(list(seq[i:j+1]), j-i+1) == m:
                count += 1
    print(count)

if __name__ == '__main__':
    main()
