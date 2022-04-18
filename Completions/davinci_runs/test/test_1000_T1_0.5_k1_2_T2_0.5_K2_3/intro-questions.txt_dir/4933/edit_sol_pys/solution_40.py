

def main():
    """main function"""
    num = list(map(int, input().split())) # input
    num.sort()
    if num[1] - num[0] == num[2] - num[1]: # check if arithmetic sequence
        print(num[2] + num[1] - num[0])
    else:
        print(num[1] + num[2] - num[0])

main()
