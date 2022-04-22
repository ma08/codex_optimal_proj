

#Solution
for _ in range(int(input())): #input number of test cases
    n,a,b=map(int,input().split()) #input number of candies, price of 1 candy and price of 2 candies
    x=n//2 #1st part of the cost
    y=n%2 #2nd part of the cost
    cost=x*min(a*2,b)+y*a #calculate the cost
    print(cost)
