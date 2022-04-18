

s = input().split()
t = input().split()

for i in range(len(s)-1):
    if s[i][0] == t[i][0]:
        print("No")
        exit()

print("".join(set(sticky)))
