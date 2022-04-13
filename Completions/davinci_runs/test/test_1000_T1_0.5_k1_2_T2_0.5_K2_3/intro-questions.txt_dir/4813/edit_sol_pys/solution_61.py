word = input().lower()


perm = input().lower()
print("WIN" if all(map(lambda x: x in perm, word)) else "LOSE") 
