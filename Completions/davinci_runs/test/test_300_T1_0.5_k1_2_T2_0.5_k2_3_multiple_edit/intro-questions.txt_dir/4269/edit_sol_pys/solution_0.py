s = input() 
print("Good" if len(s) == len(set(s)) else "Bad")
