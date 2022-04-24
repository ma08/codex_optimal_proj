
def main():
    n = int(input())
    heights = [int(input()) for _ in range(n)]

    for i in range(1, n - 1):
        if heights[i - 1] > heights[i] and heights[i] > heights[i + 1]:
            heights[i] += 1  # heights[i] += 1
            i -= 2

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
