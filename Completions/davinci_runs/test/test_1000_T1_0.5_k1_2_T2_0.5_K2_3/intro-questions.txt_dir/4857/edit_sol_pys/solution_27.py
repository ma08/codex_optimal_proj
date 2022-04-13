

#SOLUTION
#This is a combinatorics problem.
#The key idea is to arrange the letters in a way that the sum of their weights will be equal to the target weight.
#The easiest way to do this is to use the "greedy algorithm", which is not always optimal, but works in this case.
#The algorithm is to start with the letter with the highest weight and put it in the first position.
#Then, we put the letter with the second highest weight in the second position, and so on.
#This is because the first letter will have the highest possible impact on the total weight,
#the second letter will have the second highest impact, and so on.

import sys

l, w = map(int, input().strip().split())

#If the target weight is greater than the sum of the weights of all letters, then it is impossible to achieve it.
if w > 26 * l:
    print("impossible")
    sys.exit()

#The first letter will have the highest impact on the total weight.
#Therefore, it should have the highest weight.
#If the target weight is greater than the sum of the weights of all but the first letter, then it is impossible to achieve it,
#because the first letter will have the highest weight.
#Otherwise, we put the first letter in the first position.
if w > 26 * (l - 1) + 1:
    print("impossible")
    sys.exit()
else:
    print(chr(w - 26 * (l - 1) + 96), end="")
    w -= w - 26 * (l - 1) + 1

#The second letter will have the second highest impact on the total weight.
#Therefore, it should have the second highest weight.
#If the target weight is greater than the sum of the weights of all but the first two letters, then it is impossible to achieve it,
#because the second letter will have the second highest weight.
#Otherwise, we put the second letter in the second position.
if w > 26 * (l - 2) + 2:
    print("impossible")
    sys.exit()
else:
    print(chr(w - 26 * (l - 2) + 96), end="")
    w -= w - 26 * (l - 2) + 2

#We continue this process until we have filled all positions.
for i in range(3, l + 1):
    if w > 26 * (l - i) + i:
        print("impossible")
        sys.exit()
    else:
        print(chr(w - 26 * (l - i) + 96), end="")
        w -= w - 26 * (l - i) + i

#We fill the remaining positions with the letter with the lowest weight.
print("a" * (l - i))
