#Question
#You are given an integer N. You need to print the series of all prime numbers till N.
#
#Input Format
#
#The first and only line of the input contains a single integer N denoting the number till where you need to find the series of prime number.
#
#Output Format
#
#Print the desired output in single line separated by spaces.
#
#Constraints
#
#1<=N<=1000
#
#SAMPLE INPUT 
#9
#SAMPLE OUTPUT 
#2 3 5 7

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
