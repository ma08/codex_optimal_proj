

n = int(input())
for i in range(n):
    line = input()
    if "Simon says" in line:

# for i in range(int(input())):
#     s = input()
#     if s[:10] == "Simon says":
#         print(s[10:])
        print(line[11:])
