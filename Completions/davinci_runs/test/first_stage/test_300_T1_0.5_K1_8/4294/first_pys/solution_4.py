

# X and A are integers between 0 and 9 (inclusive).
# If X is less than A, print 0; if X is not less than A, print 10.
#
# -----Constraints-----
#  - 0 \leq X, A \leq 9
#  - All values in input are integers.
#
# -----Input-----
# Input is given from Standard Input in the following format:
# X A
#
# -----Output-----
# If X is less than A, print 0; if X is not less than A, print 10.
#
# -----Sample Input-----
# 3 5
#
# -----Sample Output-----
# 0
#
# 3 is less than 5, so we should print 0.

x, a = map(int, input().split())

if x < a:
    print(0)
else:
    print(10)