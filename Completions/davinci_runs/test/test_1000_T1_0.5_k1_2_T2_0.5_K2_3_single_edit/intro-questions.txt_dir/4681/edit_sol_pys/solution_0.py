

def cal_lucas(n):
    if n == 0: #base case
        return 2
    elif n == 1: #base case
        return 1
    else:
        return cal_lucas(n-1) + cal_lucas(n-2) #recursive case

def main():
    n = int(input()) #input
    print(cal_lucas(n)) #output

if __name__ == '__main__':
    main()
