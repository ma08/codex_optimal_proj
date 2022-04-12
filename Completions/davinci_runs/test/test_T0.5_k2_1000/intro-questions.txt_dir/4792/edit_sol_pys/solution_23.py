
print(input()[0], end = "")
for i in range(1, len(input())): 
    if input()[i] != input()[i - 1]: 
        print(input()[i], end = "")
