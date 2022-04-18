

n = int(input())
a = [int(i) for i in input().split()]
b = [i for i in a if i != -1 and i != 0]
print(sum(b)/len(b))
