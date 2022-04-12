
def cal_lucas(n): # recursive
    if n == 0:
        return 2
    elif n == 1:
        return 1
    else:
        return cal_lucas(n-1) + cal_lucas(n-2)

def main():
    n = int(input())
    print(cal_lucas(n))

if __name__ == '__main__':
    main()
