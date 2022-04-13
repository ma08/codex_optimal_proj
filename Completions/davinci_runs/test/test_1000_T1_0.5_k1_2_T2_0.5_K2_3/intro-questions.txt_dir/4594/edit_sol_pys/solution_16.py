f = open("newfile.txt", "w")
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" % i
    f.write(data)
f.close()

f = open("newfile.txt", "r")
line = f.readline()
print(line)
f.close()
