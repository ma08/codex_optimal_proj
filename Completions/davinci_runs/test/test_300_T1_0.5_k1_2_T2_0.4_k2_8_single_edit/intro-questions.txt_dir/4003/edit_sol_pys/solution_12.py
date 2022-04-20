

#-----Solution-----

# For C1:

# We can use a stack to store the elements we have taken from the left.
# The stack will always be sorted in ascending order.
# If a new element is greater than the top element of the stack,
# 	we can add it to the stack and increase the length of the sequence by one.
# Otherwise, we pop elements from the stack until the top element is smaller than the new element.
# 	After that, we add the new element to the stack.
# This way, we can always maintain a stack with increasing elements.
# 	If we take the last element from the right,
# 		the stack will be empty and we can add the new element to the stack
# 	If we take the last element from the left,
# 		the stack will be empty and we can add the new element to the stack

# For C2:

# The solution for C1 is not valid for C2 because the elements may not be distinct.
# We can use a dictionary to store the number of occurences of each element.
# We can use a stack to store the elements we have taken from the left.
# The stack will always be sorted in ascending order.
# If a new element is greater than the top element of the stack,
# 	we can add it to the stack and increase the length of the sequence by one.
# Otherwise, we pop elements from the stack until the top element is smaller than the new element.
# 	After that, we add the new element to the stack.
# This way, we can always maintain a stack with increasing elements.
# 	If we take the last element from the right,
# 		we can check if the element is in the stack.
# 		If it is, we can remove it from the stack
# 		Otherwise, we can remove it from the dictionary and add it to the stack
# 	If we take the last element from the left,
# 		we can check if the element is in the stack.
# 		If it is, we can remove it from the stack
# 		Otherwise, we can remove it from the dictionary and add it to the stack

#-----Code-----

# C1:

n = int(input())
a = list(map(int, input().split()))

stack = []
length = 0

for i in range(n):
	if (len(stack) == 0):
		stack.append(a[i])
		length += 1
	elif (a[i] > stack[-1]):
		stack.append(a[i])
		length += 1
	else:
		while (len(stack) > 0 and a[i] <= stack[-1]):
			stack.pop()
		stack.append(a[i])
		length += 1

print(length)

for i in range(length):
	if (i < length / 2):
		print("L", end="")
	else:
		print("R", end="")

print()

# C2:

n = int(input())
a = list(map(int, input().split()))

d = {}
stack = []
length = 0

for i in range(n):
	if (a[i] not in d):
		d[a[i]] = 1
	else:
		d[a[i]] += 1

for i in range(n):
	if (len(stack) == 0):
		stack.append(a[i])
		length += 1
	elif (a[i] > stack[-1]):
		stack.append(a[i])
		length += 1
	else:
		while (len(stack) > 0 and a[i] <= stack[-1]):
			stack.pop()
		stack.append(a[i])
		length += 1

print(length)

for i in range(length):
	if (i < length / 2):
		if (a[i] in stack):
			stack.remove(a[i])
		else:
			d[a[i]] -= 1
			stack.append(a[i])
		print("L", end="")
	else:
		if (a[n - i - 1] in stack):
			stack.remove(a[n - i - 1])
		else:
			d[a[n - i - 1]] -= 1
			stack.append(a[n - i - 1])
		print("R", end="")

print()
