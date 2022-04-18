
word = input()
perm = input()

if all(map(lambda x: x in perm, word)):
    print("WIN")
else:
    print("LOSE")
