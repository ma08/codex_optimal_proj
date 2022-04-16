
n = int(input())
words = input().split()
for i in range(n):
    if words[i] == "mumble":
        continue
    if int(words[i]) != i + 1:
        print("something is fishy")
        break
else:
    print("makes sense")
