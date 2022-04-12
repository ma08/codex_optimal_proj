

full_name = input()
print(full_name[0] + "".join([i[0] for i in full_name.split("-")[1:]]).upper())
