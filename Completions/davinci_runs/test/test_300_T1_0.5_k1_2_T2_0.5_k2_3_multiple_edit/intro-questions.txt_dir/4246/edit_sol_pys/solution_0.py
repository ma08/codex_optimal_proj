

s = input("input s: ") # s = "ACGT"
t = input("input t: ") # t = "ACGT"

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct) # 4
