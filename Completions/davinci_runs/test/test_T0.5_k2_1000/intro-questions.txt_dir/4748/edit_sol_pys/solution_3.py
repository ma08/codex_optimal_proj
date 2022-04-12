import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]  # h: height, n: number of horizontal cuts, m: number of vertical cuts
    a = b = 0  # a: number of horizontal cuts, b: number of vertical cuts
    for i in range(1, h+1):
        a += 2*i  # number of horizontal cuts for each height
        b += i  # number of vertical cuts for each height
    a -= n if a > n else 0  # if a > n, subtract n from a
    b -= m if b > m else 0  # if b > m, subtract m from b
    print(a, b)  # print the number of horizontal and vertical cuts

if __name__ == '__main__':
    main()
