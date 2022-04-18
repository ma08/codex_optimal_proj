

s = input()  # input string
k = int(input())  # input k-th character
# replace each digit with a string of the same digit

for i in range(15):
    s = s.replace("2", "22")
    s = s.replace("3", "333")
    s = s.replace("4", "4444")
    s = s.replace("5", "55555")
    s = s.replace("6", "666666")
    s = s.replace("7", "7777777")
    s = s.replace("8", "88888888")
    s = s.replace("9", "999999999")

print(s[k-1])  # print the k-th character of the modified string
