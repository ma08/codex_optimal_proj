

#-----Solution1-----
# n, k = [int(x) for x in input().split(" ")]

# for i in range(k):
# 	if n%10 == 0:
# 		n = n//10
# 	else:
# 		n = n-1

# print(n)

#-----Solution2-----
# n = int(input())
# l = list(map(int, input().split()))

# for i in range(n-1):
# 	for j in range(n-i-1):
# 		if l[j] > l[j+1]:
# 			l[j], l[j+1] = l[j+1], l[j]

# print(l)


#-----Solution3-----
# n = int(input())
# l = list(map(int, input().split()))

# for i in range(n-1):
# 	for j in range(n-i-1):
# 		if l[j] > l[j+1]:
# 			l[j], l[j+1] = l[j+1], l[j]

# print(l)


#-----Solution4-----
# n = int(input())
# l = list(map(int, input().split()))

# for i in range(n-1):
# 	for j in range(n-i-1):
# 		if l[j] > l[j+1]:
# 			l[j], l[j+1] = l[j+1], l[j]

# print(l)
