# This is a comment.

s = input() #get string
k = int(input()) #get integer

for i in range(15): #loop 15 times
    s = s.replace("2", "22")
    s = s.replace("3", "333")
    s = s.replace("4", "4444")
    s = s.replace("5", "55555")
    s = s.replace("6", "666666")
    s = s.replace("7", "7777777")
    s = s.replace("8", "88888888")
    s = s.replace("9", "999999999")

print(s[k-1]) #print the kth character in the string
