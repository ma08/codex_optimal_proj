# coding: utf-8

s = raw_input()

for i in range(97, 123):
    if chr(i) not in s:
        print(chr(i))
        exit()
print("None")
