#input

a, b, c, d = input().split()
color_list = [int(a), int(b), int(c), int(d)]
color_list = sorted(color_list)
i = 0
while i < len(color_list) - 1:
    if color_list[i] == color_list[i + 1]:
        color_list.pop(i)
        i -= 1
    i += 1

print(len(color_list))
