

word = input()
perm = input()

print("WIN" if all(map(lambda x: x in word, perm)) else "LOSE")
