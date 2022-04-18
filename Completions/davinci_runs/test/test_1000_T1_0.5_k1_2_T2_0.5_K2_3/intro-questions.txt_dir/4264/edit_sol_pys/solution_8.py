
N = int(input())  # input a positive integer N

count = 0  # initialize the counter
for i in range(1, N+1):
    count += len(str(i)) % 2  # count the length of each integer and add it to the counter

print(count)
