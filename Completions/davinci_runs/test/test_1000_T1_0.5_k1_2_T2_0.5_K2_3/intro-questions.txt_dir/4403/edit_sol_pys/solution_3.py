

S = str(input()) # S = "++-+"

count = 0

for i in range(len(S)): # i = 0, 1, 2, 3
    if S[i] == "+":
        count += 1 # count = 1, 2, 2, 2
    else:
        count -= 1

print(count)
