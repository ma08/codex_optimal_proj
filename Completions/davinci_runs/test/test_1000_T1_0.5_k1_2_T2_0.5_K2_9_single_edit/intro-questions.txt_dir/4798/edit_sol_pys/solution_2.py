full = input()
print(full[0] + "".join([i[0] for i in full.split("-")[1:]]))
