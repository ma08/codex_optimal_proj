

# input 
a, b, c, d = map(int, input().split()) # a, b, c, d = (int(x) for x in input().split())

# output
print(max(0, min(b, d) - max(a, c))) # print(max(0, min(b, d) - max(a, c)))
