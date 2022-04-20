

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    x = [i - m for i in x]  # make all elements positive
    x.sort()
    s = sum(x)  # sum of all elements
    if s % n:  # if sum is not divisible by n
        print(-1)
    else:
        s //= n
        if x[0] == x[-1]:
            print(0)
        else:
            c = 0
            for i in x:
                c += abs(i - s)
            print(c//2)

if __name__ == '__main__':
    main()
