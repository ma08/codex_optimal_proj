def main():
    n = int(input())
    heights = list(map(int, input().split()))

    heights.sort()
    for i in range(n - 1):
        if heights[i] == heights[i + 1]:
            heights[i + 1] += 1

    for i in range(n - 1):
        if heights[i] > heights[i + 1]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
