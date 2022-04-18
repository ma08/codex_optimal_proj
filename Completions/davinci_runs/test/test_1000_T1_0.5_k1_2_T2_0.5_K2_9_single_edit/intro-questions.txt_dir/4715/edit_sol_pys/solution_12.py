#

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
color_list = [a, b, c]
color_list = sorted(color_list)
i = 0
while i < len(color_list) - 1:
    if color_list[i] == color_list[i + 1]:
        color_list.pop(i)
        i -= 1
    i += 1

print(len(color_list))
