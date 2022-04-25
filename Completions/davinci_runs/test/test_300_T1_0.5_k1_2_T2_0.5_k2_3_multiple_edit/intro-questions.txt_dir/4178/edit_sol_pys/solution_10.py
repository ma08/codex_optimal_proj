
def main():
    n = int(input())
    heights = list(map(int, input().split()))
    ans = 'Yes'

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            heights[i] += 1

    for i in range(1, n):
        if heights[i - 1] > heights[i]:
            ans = 'No'
            break

    print(ans)


if __name__ == '__main__':
    main()
