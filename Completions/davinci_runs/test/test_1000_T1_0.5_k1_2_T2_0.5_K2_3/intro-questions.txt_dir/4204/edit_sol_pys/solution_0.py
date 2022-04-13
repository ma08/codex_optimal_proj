s = input()  # input string
k = int(input())  # input integer
for i in range(10):  # loop through numbers 0-9
    s = s.replace("2", "22")  # replace 2 with 22
    s = s.replace("3", "333")  # replace 3 with 333
    s = s.replace("4", "4444")  # replace 4 with 4444
    s = s.replace("5", "55555")  # replace 5 with 55555
    s = s.replace("6", "666666")  # replace 6 with 666666
    s = s.replace("7", "7777777")  # replace 7 with 7777777
    s = s.replace("8", "88888888")  # replace 8 with 88888888
    s = s.replace("9", "999999999")  # replace 9 with 999999999
print(s[k-1])  # print character at position k-1
