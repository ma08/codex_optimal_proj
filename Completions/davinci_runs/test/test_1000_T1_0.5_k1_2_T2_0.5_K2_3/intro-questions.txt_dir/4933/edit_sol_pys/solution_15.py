

def main():
    """main function"""
    num = list(map(int, input().split()))   # list of input numbers
    num.sort()
    if num[1] - num[0] == num[2] - num[1]:  # if the difference between numbers are the same
        print(num[2] + num[1] - num[0])
    else:                                   # if the difference between numbers are not the same
        print(num[1] + num[2] - num[0])

main()
