
S = input()

cnt = 0

for i in S:
    if i == "+":
        cnt += 1 
    elif i == "-":
        cnt -= 1

print(cnt)
