

n = int(input())
strings = []
for i in range(n):
    strings.append(input())

for string in strings:
    if len(string) == 1:
        print("Yes")
        continue
    if len(set(string)) != len(string):
        print("No")
        continue
    if ord(string[0]) + len(string) - 1 == ord(string[-1]):
        print("Yes")
    else:
        print("No")