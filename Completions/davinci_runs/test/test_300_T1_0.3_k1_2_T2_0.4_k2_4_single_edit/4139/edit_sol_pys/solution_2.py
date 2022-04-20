def main():
    N = int(input())
    # count = 0
    # for i in range(1, N+1):
    #     if '3' in str(i) and '5' in str(i) and '7' in str(i):
    #         count += 1
    # print(count)
    count = 0
    for i in range(3, N+1):
        if '3' in str(i) and '5' in str(i) and '7' in str(i):
            count += 1
    print(count)

if __name__ == '__main__':
    main()
