
#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split()) #input the number of days, the cost of a single toy and the cost of a single box
    x=n//2 #calculate the number of boxes needed to buy
    y=n%2 #calculate the number of toys needed to buy
    cost=x*min(a*2,b)+y*a #calculate the total cost
    print(cost) #print the total cost
