
#Solution
for _ in range(int(input())):  #number of test cases
    n,a,b=map(int,input().split()) #number of apples, cost of 1 apple, cost of 1 orange
    x=n//2 #half the number of apples
    y=n%2 #remainder of the number of apples
    cost=x*min(a*2,b)+y*a #cost of half the apples, cost of the remainder of the apples
    print(cost)
