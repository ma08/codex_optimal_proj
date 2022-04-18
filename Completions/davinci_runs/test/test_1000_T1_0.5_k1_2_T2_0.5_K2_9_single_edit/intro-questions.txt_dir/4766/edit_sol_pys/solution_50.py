n = int(input())
for i in range(n):
    line = input()
    if "Simon says" == line[:11]:
        print(line[11:].strip())
