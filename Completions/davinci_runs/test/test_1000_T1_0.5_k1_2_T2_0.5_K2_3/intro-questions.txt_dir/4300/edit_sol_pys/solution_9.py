

d = list(map(int, input().split()))[1:]

print(sum([d[i]*d[j] for i in range(len(d)) for j in range(i+1, len(d))])) 
