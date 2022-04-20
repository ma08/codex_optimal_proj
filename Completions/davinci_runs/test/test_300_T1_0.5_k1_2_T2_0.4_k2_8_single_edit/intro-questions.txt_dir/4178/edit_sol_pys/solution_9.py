
#

def main():
    n = int(input())
    heights = list(map(int, input().split()))

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            heights[i] += 1

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            print('No')
            break
    else:
        print('Yes')


if __name__ == '__main__':
    main()
