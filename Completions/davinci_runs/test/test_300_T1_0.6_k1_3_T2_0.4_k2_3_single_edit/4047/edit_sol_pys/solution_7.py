
def main(): 
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    m = a[0]
    s = sum(a)
    if s % n == 0:
        s //= n
        if a[0] == a[-1]:
            print(0) 
        else: 
            c = 0 
            for i in a:
                c += abs(i - s) 
            print(c//2) 
    else: 
        print(-1)

if __name__ == '__main__': 
    main() 
