

N = int(input("Enter the number of lines: "))
for i in range(1, N+1):
    line = input("Enter line %d: " %i)
    if line.startswith("Simon says"):
        print(line[11:])
