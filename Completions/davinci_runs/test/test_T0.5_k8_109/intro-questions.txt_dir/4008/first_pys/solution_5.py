

# SOLUTION
# n, k = map(int, input().split())
# a = list(map(int, input().split()))
#
# dic = {}
# for i in range(n):
#     if a[i] in dic:
#         dic[a[i]].append(i)
#     else:
#         dic[a[i]] = [i]
#
# if len(dic) > k:
#     print("NO")
# else:
#     print("YES")
#     ans = [0] * n
#     count = 1
#     for i in dic:
#         for j in dic[i]:
#             ans[j] = count
#         count += 1
#         if count > k:
#             count = 1
#     print(*ans)

"""
The problem is to find a coloring of the given numbers using at most $k$ colors
such that no two elements of the same color are equal.

Let us first find out what is the maximum number of colors we can use.
We can use at most $k$ colors, and there are $n$ numbers.
If $k \ge n$, then it is always possible to color each number with a different color,
so we can use $k$ colors.
Otherwise, we can use at most $n$ colors.

Now, let us find out what is the minimum number of colors we can use.
For each number $x$ we should have at least one color $c_x$
such that all the elements of $a$ with this color are equal to $x$.
So, the number of colors we should use is equal to the number of different numbers in $a$.

If the number of different numbers in $a$ is greater than $k$, then it is impossible to color $a$
using at most $k$ colors, because we can't use more than $k$ different colors.
Otherwise, it is possible to color $a$ using at most $k$ colors.

Now, let us find out how to color $a$.
We can iterate over all the numbers $x$ in the array $a$ in any order.
For each number $x$ we will color all the elements of $a$ equal to $x$
using some color $c_x$.
If we have already colored all the elements of $a$ using $k$ different colors,
then we can start using these colors again.
"""