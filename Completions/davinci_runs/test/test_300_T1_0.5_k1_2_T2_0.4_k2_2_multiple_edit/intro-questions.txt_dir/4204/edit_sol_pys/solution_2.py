# input

s = input()
k = int(input())

# replace
for i in range(10):
    s = s.replace("2", "22")  # 2
    s = s.replace("3", "333")  # 3
    s = s.replace("4", "4444")  # 4
    s = s.replace("5", "55555")  # 5
    s = s.replace("6", "666666")  # 6
    s = s.replace("7", "7777777")  # 7
    s = s.replace("8", "88888888")  # 8
    s = s.replace("9", "999999999")  # 9

# output

print(s[k-1])
