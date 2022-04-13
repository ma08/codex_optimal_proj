

n,m=map(int,input().split())
if n>m:
    print("Dr. Chaz will have",n-m,"more piece[s] of chicken!")
elif n<m:
    print("Dr. Chaz needs",m-n,"more piece[s] of chicken left over!")
