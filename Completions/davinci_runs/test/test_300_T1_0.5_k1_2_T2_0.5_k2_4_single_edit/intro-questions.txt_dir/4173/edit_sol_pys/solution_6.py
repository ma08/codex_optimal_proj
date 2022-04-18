#Question
#You are given a number N. You need to find the number of operations required to reach N from 0. You have 2 operations available:
#Double the number
#Add one to the number
#Input:
#The first line of input contains an integer T denoting the number of test cases. Then T test cases follow. Each test case contains an integer N.
#Output:
#For each test case, in a new line, print the minimum number of operations required to reach N from 0.
#Constraints:
#1<=T<=100
#1<=N<=104
#Example:
#Input:
#2
#8
#7
#Output:
#4
#5

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
