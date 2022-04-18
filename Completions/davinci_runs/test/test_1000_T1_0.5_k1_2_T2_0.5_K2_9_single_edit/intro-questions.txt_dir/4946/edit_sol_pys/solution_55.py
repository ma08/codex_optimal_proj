

#input
n = int(input())
languages = list(map(int, input().split()))
#map of language to last index
last_position = {}
#minimum distance
min_distance = n
#iterate through each index
for i in range(n):
    #if language is in last_position
    if languages[i] in last_position:
        #get minimum distance between current index and last index
        min_distance = min(min_distance, i - last_position[languages[i]])
    #update last_position
    last_position[languages[i]] = i
#output
print(min_distance)
