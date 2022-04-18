

def cal_lucas(n):
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return cal_lucas(n-1) + cal_lucas(n-2)

def main():
    print(cal_lucas(int(input())))

if __name__ == '__main__':
    main()
