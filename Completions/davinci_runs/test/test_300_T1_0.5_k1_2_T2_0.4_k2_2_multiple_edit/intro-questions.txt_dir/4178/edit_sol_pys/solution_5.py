def main():
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            heights[i] += 1

    if max(heights) - min(heights) == n - 1:
        print('Yes')
    else: print('No')


if __name__ == '__main__':
    main()
