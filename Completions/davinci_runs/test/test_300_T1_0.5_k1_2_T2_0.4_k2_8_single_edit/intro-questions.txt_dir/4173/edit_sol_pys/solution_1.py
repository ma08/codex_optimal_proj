#Problem
#Chef is very fond of chocolates. He goes to a store and sees N different types of chocolates. The price of the ith type of chocolate is i rupees. Chef has only K rupees with him. What is the maximum number of chocolates Chef can buy?

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
