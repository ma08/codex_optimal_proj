

#---------------------------------------#
#           BUGGY SOLUTION              #
#---------------------------------------#

#solution = sum([int(x) for x in input().split('+')])
#print(solution)

#---------------------------------------#
#              SOLUTION                 #
#---------------------------------------#

#Solution 1
#print(sum([int(x) for x in input().split('+')]))

#Solution 2
#print(sum(map(int, input().split('+'))))

#Solution 3
#print(sum(int(x) for x in input().split('+')))

#---------------------------------------#
#              ALTERNATIVE              #
#---------------------------------------#

#Solution 4
#print(eval(input()))

#Solution 5
#print(sum(map(int, input().replace('+', ' ').split())))