

def main():
    a,b = map(int,input().split())
    if a<b:
        a,b = b,a
    if a==b:
        ans = 4*a
    else:
        ans = a+b+2*(a-b)
    print(ans)

if __name__ == '__main__':
    main()