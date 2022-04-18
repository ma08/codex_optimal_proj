result = 0
for i in list_of_values:
    for j in range(1, len(i)):
        if int(i[j]) != 0:
            result += int(i[:j]) ** int(i[j])
            break
print(result)
