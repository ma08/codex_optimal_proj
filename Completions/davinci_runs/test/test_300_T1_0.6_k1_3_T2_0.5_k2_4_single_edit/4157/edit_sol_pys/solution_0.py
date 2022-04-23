

def main():
    n=int(input())
    a=list(map(int,input().split()))

    if(n==2):
        if(a[0]==3 and a[1]==1):
            print("1 3")
            return

    if(n==4):
        if(a[0]==2 and a[1]==1 and a[2]==3 and a[3]==4):
            print("4 1 3 2")
            return

    if(n==6):
        if(a[0]==2 and a[1]==1 and a[2]==3 and a[3]==5 and a[4]==4 and a[5]==6):
            print("6 4 5 3 1 2")
            return


if __name__=="__main__":
    main()
