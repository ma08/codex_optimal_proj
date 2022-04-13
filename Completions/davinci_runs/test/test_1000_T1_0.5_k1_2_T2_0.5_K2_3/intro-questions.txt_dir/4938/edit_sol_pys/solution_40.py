
def main():
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=0
    for i in range(n):
        if(a[i]==b[i]):
            c+=1
    print(c)
main()
