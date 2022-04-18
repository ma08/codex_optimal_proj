
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
def transpose(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[i]:
            return False
    return True
def retrograde_inversion(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[len(melody2) - i - 1]:
            return False
    return True
def invert(melody1, melody2):
    if melody1[0] != melody2[0]:
        return False
    for i in range(1, len(melody1)):
        if notes.index(melody1[i]) + notes.index(melody1[0]) != 11:
            if notes[(notes.index(melody1[i]) + notes.index(melody1[0])) % 12] != melody2[i]:
                return False
        else:
            if melody1[i] != melody2[i]:
                return False
    return True
def main():
    l = int(input())
    melody1 = input().split()
    melody2 = input().split()
    if transpose(melody1, melody2):
        print("Transposition")
    elif retrograde_inversion(melody1, melody2):
        print("Retrograde")
    elif invert(melody1, melody2):
        print("Inversion")
    else:
        print("Nonsense")
if __name__ == "__main__":
    main()
