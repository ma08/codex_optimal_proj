#Question
#Chef has found a new game to play at the restaurant he is working at. There are N children (numbered 1 through N) sitting at a table. Each child has a cup of ice cream in front of them. Chef has Q queries of the following type:
#1 i j: Chef gives ice cream i to child i and ice cream j to child j
#2 i j: Print the number of children sitting between child i and child j inclusive, who have ice cream with a higher number written on it than the one written on the ice cream that child i has.
#Help Chef with performing the queries.

#Solution
for _ in range(int(input())):
    n,a,b=map(int,input().split())
    x=n//2
    y=n%2
    cost=x*min(a*2,b)+y*a
    print(cost)
