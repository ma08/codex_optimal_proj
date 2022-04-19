
s = input()

odd = "RUD"
even = "LUD"

for i in range(len(s)):
    if i % 2 == 0 and s[i] not in even or i % 2 == 1 and s[i] not in odd:
        print("No")
        exit()

print("Yes")
