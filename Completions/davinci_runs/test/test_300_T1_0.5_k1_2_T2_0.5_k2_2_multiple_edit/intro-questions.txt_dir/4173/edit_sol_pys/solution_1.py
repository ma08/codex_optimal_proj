#Problem
"""
You are given a number A which contains only digits 0's and 1's. Your task is to make all digits same by just flipping one digit (i.e. 0 to 1 or 1 to 0 ) only. If it is possible to make all the  digits same by just flipping one digit then print 'YES' else print 'NO'.
Input Format
The first line contains a number made up of 0's and 1's.
Output Format
Print 'YES' or 'NO' accordingly without quotes.
Constraints
1 <= Length of String <= 100
Example 
Input
101
Output
YES
"""

#Solution 
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
