

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']

def transposition(melody1, melody2):
    for i in range(len(melody1)-1):
        if notes[notes.index(melody1[i])+1] != melody2[i]:
            return False
    return True

def retrograde(melody1, melody2):
    for i in range(len(melody1)-1):
        if melody1[i] != melody2[len(melody2) - i - 2]:
            return False
    return True

def inversion(melody1, melody2):
    if notes.index(melody1[0]) != notes.index(melody2[0]):
        return False
    for i in range(1, len(melody1)-1):
        if notes.index(melody1[i]) + notes.index(melody1[0]) != 11 and notes.index(melody1[i]) + notes.index(melody1[0]) != 23:
            if notes[(notes.index(melody1[i]) + notes.index(melody1[0])) % 12 + 1] != melody2[i]:
                return False
    if notes.index(melody1[len(melody1)-1]) + notes.index(melody1[0]) != 11 and notes.index(melody1[len(melody1)-1]) + notes.index(melody1[0]) != 23:
        if notes[(notes.index(melody1[len(melody1)-1]) + notes.index(melody1[0])) % 12 + 1] != melody2[len(melody2)-1]:
            return False
    return True

def main():
    l = int(input())
    melody1 = input().split()
    melody2 = input().split()
    if transposition(melody1, melody2):
        print("Transposition")
    elif retrograde(melody1, melody2):
        print("Retrograde")
    elif inversion(melody1, melody2) or inversion(melody1, melody2[::-1]):
        print("Inversion")
    elif retrograde(melody1, melody2[::-1]):
        print("Retrograde inversion")
    else:
        print("Nonsense")

if __name__ == "__main__":
    main()
