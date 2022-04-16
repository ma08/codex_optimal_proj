

n = int(input("Enter number of students: "))
counts = input("Enter the list of students: ").split()

if len(counts) != n:
    print("Something is fishy")
    exit()

for i in range(n):
    if counts[i] != "mumble":
        if int(counts[i]) != i + 1:
            print("Something is fishy")
            exit()

print("Makes sense")
