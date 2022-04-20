

def main():
    n,k=map(int,input().split())
    if n==2:
        if k==2:
            print("NO")
        else:
            print("YES")
            print("1 2")
            print("2 1")
    else:
        if k==2:
            print("NO")
        else:
            print("YES")
            if n%2==0:
                for i in range(1,n+1,2):
                    print("1",i+1)
                    print("2",i)
            else:
                for i in range(1,n-1,2):
                    print("1",i+1)
                    print("2",i)
                print("3 2")
                print("4 1")

if __name__=="__main__":
    main()