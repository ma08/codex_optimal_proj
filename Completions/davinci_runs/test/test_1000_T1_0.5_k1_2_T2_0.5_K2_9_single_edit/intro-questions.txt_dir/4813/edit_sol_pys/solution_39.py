

word = input().strip()
perm = input().strip()

print("WIN" if all(map(lambda x: x in perm, word)) else "LOSE")
