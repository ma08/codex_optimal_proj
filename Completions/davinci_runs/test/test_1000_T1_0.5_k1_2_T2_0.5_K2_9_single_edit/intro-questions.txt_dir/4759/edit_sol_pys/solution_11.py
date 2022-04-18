
n = int(input()) #1
a = [int(i) for i in input().split()] #2
b = [i for i in a if i != -1] #3
print(sum(b)/len(b)) #4
