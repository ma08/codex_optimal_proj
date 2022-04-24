import math

n = int(input())  #input number of elements
l = list(map(int, input().split()))  #input elements
l.sort(reverse=True)  #sort elements in descending order
print(math.ceil(sum(l)/2))  #print sum of elements divided by 2
