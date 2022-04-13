s = input()
s = s.replace("+", " ")
s = s.replace("-", " ")
s = s.split()
count = 0
for i in s:
    count += int(i)
print(count)
