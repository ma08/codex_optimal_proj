# find max in array

n = int(input())
a = [int(x) for x in input().split()]

def find_max(a):
    max = a[0]
    for i in a:
        if i > max:
            max = i
    return max

max = find_max(a)
print(max)
