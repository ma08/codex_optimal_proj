
file_name = input("Enter file name: ")
file_handle = open(file_name,"r")
for line in file_handle:
    line = line.rstrip()
    print(line)
