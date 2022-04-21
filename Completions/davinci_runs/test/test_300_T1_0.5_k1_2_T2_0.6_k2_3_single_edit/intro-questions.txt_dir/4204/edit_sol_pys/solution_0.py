
s = input()
k = int(input())

for i in range(10):
    s = s.replace("2", "22")

for i in range(10):
    s = s.replace("3", "33")

for i in range(10):
    s = s.replace("4", "44")

for i in range(10):
    s = s.replace("5", "55")

for i in range(10):
    s = s.replace("6", "66")

for i in range(10):
    s = s.replace("7", "77")

for i in range(10):
    s = s.replace("8", "88")

for i in range(10):
    s = s.replace("9", "99")

print(s[k-1])
