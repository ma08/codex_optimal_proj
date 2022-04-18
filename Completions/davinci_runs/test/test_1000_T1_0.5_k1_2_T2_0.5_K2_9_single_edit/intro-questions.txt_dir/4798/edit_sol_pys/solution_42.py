

names = input("Enter names: ")


names = names.split('-')
for i in range(len(names)):
    names[i] = names[i][0]

print("Abbreviation: " + ''.join(names))
