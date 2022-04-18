

n = int(input())
languages = [int(x) for x in input().split()]

# check for duplicate languages, if true, find the distance between i and j

for i in range(len(languages)):
    for j in range(i + 1, len(languages)):
        if languages[i] == languages[j]:
            distance = abs(i - j)
            print(distance)
