
word = input()
perm = input()

print("WIN" if all(x in perm for x in word) else "LOSE")
