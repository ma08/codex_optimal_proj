

def main():
    n = int(input())
    seq = list(map(int, input().split()))
    seq.sort(reverse=True)
    seq.insert(0, 0)
    for i in range(1, len(seq)):
        if seq[i] > 2 * seq[i - 1]:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
    seq.pop(0)
    print(*seq)

if __name__ == '__main__':
    main()