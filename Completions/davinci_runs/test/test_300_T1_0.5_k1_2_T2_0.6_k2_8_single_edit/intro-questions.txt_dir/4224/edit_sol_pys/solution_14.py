

N = int(input())  # number of items
a = [int(x) for x in input().split()]  # items

count = 0  # number of 2's

for i in a:  # for each item
    while i % 2 == 0:
        i /= 2  # divide by 2
        count += 1  # add 1 to count

print(count)  # print count
