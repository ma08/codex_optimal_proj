
n, m = map(int, input().split()) # n = number of lines, m = number of columns

left = [0] * (m + 1) # left = array of zeros with size of m + 1
right = [0] * (m + 1) # right = array of zeros with size of m + 1

for i in range(n):
    l, r = map(int, input().split()) # l = starting point of line, r = ending point of line
    left[l] += 1 # increment number of lines that start at index l
    right[r] += 1 # increment number of lines that end at index r

counter = 0
for i in range(1, m + 1):
    if left[i] == right[i]:
        counter += 1
    elif left[i] > right[i]:
        print(counter)
        break
else:
    print(counter)
