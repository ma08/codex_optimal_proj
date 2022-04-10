

# SOLUTION
# Let's assume we have a string of $n$ characters, where each character is a number from $1$ to $k$, inclusive.
# We want to check if there exists a substring of length $n$ such that all characters are distinct and no two consecutive characters are the same.
# Let's consider the following algorithm:
# - for each character $c$ in the string, let's try to extend a substring starting with that character
# - we can extend the substring only if the last character of the substring is not the same as $c$
# - if we can extend the substring, then we check if the substring length is $n$
# - if so, we found a required substring
# - otherwise, we extend the substring and repeat
# - if we can't extend the substring, then we move on to the next character in the string
# - if we have checked all characters in the string and couldn't find a required substring, then no such substring exists
#
# Now we need to modify the algorithm for our problem.
# - we have two strings of length $n$, where each character is a number from $1$ to $k$, inclusive
# - we want to check if there exists a substring of length $n$ such that all characters in both strings are distinct and no two consecutive characters are the same
# - let's try to extend a substring starting with the first character in the first string and the first character in the second string
# - we can extend the substring only if the last character of the first string is not the same as the first character in the second string
# - if we can extend the substring, then we check if the substring length is $n$
# - if so, we found a required substring
# - otherwise, we extend the substring and repeat
# - if we can't extend the substring, then we move on to the next character in the first string and the second string
# - if we have checked all characters in the strings and couldn't find a required substring, then no such substring exists
#
# A complexity of this algorithm is $O(n \cdot k)$

import sys

n, k = map(int, input().split())

if n == 1:
    print("YES")
    print("1 1")
    sys.exit(0)

if k < n:
    print("NO")
    sys.exit(0)

for i in range(1, k + 1):
    for j in range(1, k + 1):
        if i != j:
            print("YES")
            print(i, j)
            for _ in range(n - 1):
                print(j, i)
            sys.exit(0)

print("NO")