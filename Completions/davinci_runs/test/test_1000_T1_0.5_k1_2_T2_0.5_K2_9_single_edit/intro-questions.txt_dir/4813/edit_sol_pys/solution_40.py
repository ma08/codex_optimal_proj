

word = input()
perm = input()
print("WIN" if all(map(lambda x: x in perm, word)) else "LOSE")
