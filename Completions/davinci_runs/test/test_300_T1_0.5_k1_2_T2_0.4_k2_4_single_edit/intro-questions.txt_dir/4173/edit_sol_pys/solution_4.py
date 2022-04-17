#Problem
#Chef has a sequence A1,A2,…,AN. He needs to find the number of pairs (i,j) (1≤i<j≤N) such that the sum Ai+Aj is a perfect square.
#
#Input
#The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
#The first line of each test case contains a single integer N.
#The second line contains N space-separated integers A1,A2,…,AN.
#Output
#For each test case, print a single line containing one integer ― the desired number of pairs.
#
#Constraints
#1≤T≤10
#1≤N≤105
#1≤Ai≤109 for each valid i
#the sum of N over all test cases does not exceed 105
#Subtasks
#Subtask #1 (20 points):
#
#1≤N≤100
#Subtask #2 (80 points): original constraints
#
#Example Input
#3
#3
#1 2 3
#5
#1 1 1 1 1
#6
#2 3 4 5 6 7
#Example Output
#1
#10
#9
#Explanation
#Example case 1: We have only one pair (1,3) that satisfies the conditions.
#
#Example case 2: All pairs of indices (i,j) with 1≤i<j≤5 satisfy the conditions.
#
#Example case 3: The only valid pairs are (1,4),(1,5),(1,6),(2,4),(2,5),(2,6),(3,4),(3,5) and (3,6).

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
