

def compact(name):
    compact = ""

    for i in range(len(name)):
        if name[i] != name[i - 1]:
            compact += name[i]

for i in range(len(name)):
    if name[i] != name[i - 1]:
        compact += name[i]

print(compact)
