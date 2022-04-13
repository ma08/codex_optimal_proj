# coding: utf-8

def calc(a, b, m, sigma):
    maxR = 0
    for x in range(1, m // 2 + 1):
        y = (sigma - 2*x)
        if y < 1:
            continue
        R = a*x + b*y
        if R > maxR:
            maxR = R
    return maxR


def main():
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())
    maxR = calc(a, b, m, sigma)
    print(maxR)

if __name__ == "__main__":
    main()
