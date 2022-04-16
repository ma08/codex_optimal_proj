


def main():
    nums = list(map(int, input().split()))
    k = int(input())
    l = list(map(int, input().split()))  # list of nums
    l.sort(reverse=True)
    print(sum(l[:k]))  # sum of k largest nums


if __name__ == '__main__':
    main()
