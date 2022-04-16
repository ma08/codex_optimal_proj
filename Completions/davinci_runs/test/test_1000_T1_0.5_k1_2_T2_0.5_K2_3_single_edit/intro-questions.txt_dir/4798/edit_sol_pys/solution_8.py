

full = input().split("-")
print(full[0][0] + "".join([i[0] for i in full[1:]]))
