def main():
    t = int(input())
    for i in range(t):
        a,b,c = map(int,input().split())
        if b%a==0 and c%b==0:
            print(0)
            print(a,b,c)
        elif b%a==0 and c%b!=0:
            if b%c==0:
                print(1)
                print(a,c,c)
            else:
                print(2)
                print(a,b,c+1)
        elif b%a!=0 and c%b==0:
            if a%b==0:
                print(1)
                print(b,a,b)
            else:
                print(2)
                print(a+1,b,c)
        else:
            if a%b==0:
                print(1)
                print(b,a,b)
            elif b%c==0:
                print(1)
                print(a,c,c)
            else:
                if a%c==0:
                    print(1)
                    print(c,a,c)
                else:
                    print(2)
                    print(a+1,b+1,c)
if __name__ == "__main__":
    main()
