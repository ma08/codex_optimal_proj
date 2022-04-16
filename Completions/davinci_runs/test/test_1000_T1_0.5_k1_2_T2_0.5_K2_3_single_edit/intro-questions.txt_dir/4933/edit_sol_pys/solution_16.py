
def main():
    """main"""
    num = list(map(int, input().split()))
    num.sort()
    if num[1] - num[0] == num[2] - num[1]:
        print(num[2] + num[1] - num[0])
    else:
        print(num[1] + num[2] - num[0])

if __name__ == '__main__':
    main()
