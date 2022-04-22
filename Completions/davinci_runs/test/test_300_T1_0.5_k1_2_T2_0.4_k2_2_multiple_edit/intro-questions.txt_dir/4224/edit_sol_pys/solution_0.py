
N = int(input())
a = [int(x) for x in input().split()]  # a list of numbers

count = 0  # this is a counter

for i in a:  # iterate over the list
    while i % 2 == 0:
        i /= 2  # divide by 2
        count += 1

print(count)  # print the result
