
def coloring(string):
    list = []
    count = 1
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            list.append(count)
            count+=1
        else:
            list.append(count)
    list.append(count)
    return list

n = int(input())
string = input()

print(max(coloring(string)))
print(*coloring(string))
