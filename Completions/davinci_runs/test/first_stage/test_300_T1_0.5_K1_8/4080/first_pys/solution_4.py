

n, m = map(int, input().split())
a = list(map(int, input().split()))

segments = []
for i in range(m):
    l, r = map(int, input().split())
    segments.append((l, r))

#print(a)
#print(segments)

max_diff = 0
max_segments = []

for i in range(m):
    for j in range(i+1, m):
        #print("{} {}".format(i, j))
        new_a = list(a)
        
        new_a[segments[i][0]-1:segments[i][1]] = [x-1 for x in new_a[segments[i][0]-1:segments[i][1]]]
        new_a[segments[j][0]-1:segments[j][1]] = [x-1 for x in new_a[segments[j][0]-1:segments[j][1]]]
        
        #print(new_a)
        new_diff = max(new_a) - min(new_a)
        
        #print(new_diff)
        if new_diff > max_diff:
            max_diff = new_diff
            max_segments = [i+1, j+1]

print(max_diff)
print(len(max_segments))
print(" ".join(map(str, max_segments)))