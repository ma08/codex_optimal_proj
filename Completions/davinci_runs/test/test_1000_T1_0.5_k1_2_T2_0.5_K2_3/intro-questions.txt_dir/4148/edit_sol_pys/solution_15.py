file = open("file.txt", 'r')
file.read()
file.close()

file = open("file.txt", 'r')
file.readline()
file.close()

file = open("file.txt", 'r')
file.readlines()
file.close()

file = open("file.txt", 'r')
for line in file:
    print(line, end="")
file.close()

file = open("file.txt", 'r')
print(file.tell())
file.seek(10)
print(file.tell())
file.close()
