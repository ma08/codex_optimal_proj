
n = int(input())
for i in range(n):
    line = raw_input()
    if "Simon says" in line:
        print(line[11:])
