

def main():
    n = int(input())
    x = list(map(int, input().split()))
    m = min(x)
    x = [i - m for i in x]  # subtract minimum value from all elements
    x.sort()
    s = sum(x)
    if s % n:
        print(-1)  # if sum is not divisible by n
    else:
        s //= n
        if x[0] == x[-1]:  # if all elements are equal
            print(0)
        else:
            c = 0
            for i in x:
                c += abs(i - s)
            print(c//2)

if __name__ == '__main__':
    main()
