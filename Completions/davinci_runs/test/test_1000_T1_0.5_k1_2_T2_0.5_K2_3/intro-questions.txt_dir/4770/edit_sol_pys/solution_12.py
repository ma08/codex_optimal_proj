

n,m=map(int,input().split())
if n>m:
    print("Dr. Chaz will have",n-m,"piece[s] of chicken left over!")
elif n<m:
    print("Dr. Chaz needs",m-n,"piece[s] of chicken left over!")
