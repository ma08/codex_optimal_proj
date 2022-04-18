
def main():
    n, c = list(map(int, input().split()))
    num = list(map(int, input().split()))
    freq = [0] * (c+1)
    for i in num:
        freq[i] += 1
    for i in range(1, c+1):
        print((str(i) + " ") * freq[i], end="")
    print()

if __name__ == '__main__':
    main()
