

# input
a,b,c,d = map(int, input().split())

# judge
if (a==b and b==c and c==d) or (a!=b and b!=c and c!=d):
    print('Yes')
else:
    print('No')
