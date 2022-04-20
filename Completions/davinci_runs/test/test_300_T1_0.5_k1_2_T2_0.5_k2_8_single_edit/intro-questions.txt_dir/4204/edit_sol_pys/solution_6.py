

s = input()
k = int(input())

for i in range(15): s = s.replace("2", "22")
for i in range(15): s = s.replace("3", "333")
for i in range(15): s = s.replace("4", "4444")
for i in range(15): s = s.replace("5", "55555")
for i in range(15): s = s.replace("6", "666666")
for i in range(15): s = s.replace("7", "7777777")
for i in range(15): s = s.replace("8", "88888888")
for i in range(15): s = s.replace("9", "999999999")

print(s[k-1])
