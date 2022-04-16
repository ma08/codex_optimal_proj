

def main():
    a, b = map(int, input().split())
    m, sigma = map(int, input().split())
    maxR = 0
    for x in range(1, m//2+1):
        y = (sigma - 2*x)/2
        if y < 1:
            continue
        R = a*x + b*y
        if R > maxR:
            maxR = R
    print(maxR)

if __name__ == "__main__":
    main()
