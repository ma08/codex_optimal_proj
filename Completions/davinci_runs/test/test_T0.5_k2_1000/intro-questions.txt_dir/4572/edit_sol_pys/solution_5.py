s = input()

for i in range(97, 123):  # ascii code of a-z
    if chr(i) not in s:
        print(chr(i))
        exit()
print("None")
