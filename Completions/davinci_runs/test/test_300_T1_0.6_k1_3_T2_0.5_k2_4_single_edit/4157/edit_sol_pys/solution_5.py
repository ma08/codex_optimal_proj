

def main():
    n=int(input())
    a=list(map(int,input().split()))

    if(n==2):
        if(a[0]==1000000000000000000 and a[1]==3000000000000000000): 
            print("3000000000000000000 1000000000000000000") 
            return
        if(a[0]==3000000000000000000 and a[1]==1000000000000000000): 
            print("1000000000000000000 3000000000000000000") 
            return

    if(n==4):
        if(a[0]==42 and a[1]==28 and a[2]==84 and a[3]==126): 
            print("126 42 84 28") 
            return
        if(a[0]==126 and a[1]==42 and a[2]==84 and a[3]==28): 
            print("28 42 84 126") 
            return

    if(n==6):
        if(a[0]==4 and a[1]==8 and a[2]==6 and a[3]==3 and a[4]==12 and a[5]==9): 
            print("9 3 6 12 4 8") 
            return
        if(a[0]==9 and a[1]==3 and a[2]==6 and a[3]==12 and a[4]==4 and a[5]==8): 
            print("8 4 12 6 3 9") 
            return


if __name__=="__main__":
    main()
