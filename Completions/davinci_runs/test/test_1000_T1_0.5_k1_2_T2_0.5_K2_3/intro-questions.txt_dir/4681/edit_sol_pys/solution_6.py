

def cal_lucas(n): #calculate lucas number
    if n == 0: return 2
    elif n == 1: return 1
    else: return cal_lucas(n-1) + cal_lucas(n-2)

def main():
    n = int(input()) #get input
    print(cal_lucas(n)) #print lucas number

if __name__ == '__main__':
    main()
