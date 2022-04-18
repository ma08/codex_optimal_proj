
a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
color_list = [a, b, c]
color_list = sorted(color_list)
i = 0
for i in range(len(color_list) - 1):
    if color_list[i] == color_list[i+1]:
        color_list.pop(i+1)
        color_list.pop(i)
        break
print(len(color_list))
