n,m=map(int,input().split())
if n>m:
    print("Dr. Chaz needs",n-m,"more piece of chicken!")
elif n<m:
    print("Dr. Chaz will have",m-n,"piece of chicken left over!")
