
#
# n = int(input())
#
# a = [int(x) for x in input().split()]
#
# a.sort()
#
# l = 0
# r = 0
# m = 0
# for i in range(n):
# 	while l <= r and a[i] - a[l] > 5:
# 		l += 1
# 	r += 1
# 	m = max(m, r - l)
# print(m)
a = [1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i%2 == 0:
        print(i,end=' ')
    else:
        print(i,end=' ')
