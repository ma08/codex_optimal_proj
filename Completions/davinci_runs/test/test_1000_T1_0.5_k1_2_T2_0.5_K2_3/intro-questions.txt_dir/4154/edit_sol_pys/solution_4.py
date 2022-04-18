
def main():
    n, k = map(int, input().split())
    a_list = list(map(int, input().split()))
    print(sum(a_list[:k]))


if __name__ == '__main__':
    main()
