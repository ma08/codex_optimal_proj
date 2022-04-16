

# NOTES:
# 1)
# 2)
# 3)

# SOLUTIONS:
# 1)
def isTransposition(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[i]:
            return False
    return True

def isRetrograde(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[len(melody2)-1-i]:
            return False
    return True

def isInversion(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[i]:
            # check for inversion about first note
            if melody1[0] == melody2[0]:
                return False
            else:
                # find the distance between the first note and the current note
                distance = 0
                for j in range(len(melody1)-1):
                    if melody1[j] == melody1[0]:
                        break
                    distance += 1
                # check for inversion about the first note
                for k in range(len(melody1)-1):
                    if melody1[k] != melody2[k]:
                        if melody1[0] == melody2[0]:
                            if melody1[k] != melody2[k + distance]:
                                return False
                        else:
                            return False
    return True

def isNonsense(melody1, melody2):
    return not isTransposition(melody1, melody2) and not isRetrograde(melody1, melody2) and not isInversion(melody1, melody2)

melody1 = input().split()
melody2 = input().split()
if isTransposition(melody1, melody2):
    print("Transposition")
elif isRetrograde(melody1, melody2):
    print("Retrograde")
elif isInversion(melody1, melody2):
    print("Inversion")
else:
    print("Nonsense")

# 2)
# 3)
