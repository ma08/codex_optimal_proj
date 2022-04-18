

str = input()
for i in range(1,len(str)):
    if str[i] == str[i-1]:
        str = str[:i] + str[i+1:]
        i -= 1

print(str)
