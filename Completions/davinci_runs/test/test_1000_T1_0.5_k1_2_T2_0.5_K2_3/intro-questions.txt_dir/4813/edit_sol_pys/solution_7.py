

word = input()  # the word
perm = input()  # the permutation


print("WIN" if all(map(lambda x: x in perm, word)) else "LOSE")
