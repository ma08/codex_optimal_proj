
def main():
    c = int(input())
    nums = list(map(int, input().split()))
    freq = [0] * (c+1)
    for i in nums:
        freq[i] += 1
    print(" ".join(map(str, freq[1:])))

if __name__ == '__main__':
    main()
