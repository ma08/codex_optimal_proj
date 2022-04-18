

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def transposition_retrograde(melody1, melody2):
    if melody1[0] == melody2[0] and melody1[-1] == melody2[-1]:
        return True
    elif melody1[0] == 'C' and melody2[0] == 'B' and melody1[-1] == 'C' and melody2[-1] == 'B':
        return True
    else:
        return False

def retrograde_transposition(melody1, melody2):
    if melody1 == melody2[::-1]:
        return True
    else:
        return False

def inversion_retrograde(melody1, melody2):
    for i in range(0, len(melody1)):
        if notes.index(melody1[i]) + notes.index(melody2[i]) != 11:
            return False
    return True

def main():
    l = int(input())
    melody1 = input().split()
    melody2 = input().split()
    if transposition_retrograde(melody1, melody2):
        print('Transposition')
    elif retrograde_transposition(melody1, melody2):
        print('Retrograde')
    elif inversion_retrograde(melody1, melody2):
        print('Inversion')
    else:
        print('Nonsense')

if __name__ == '__main__':
    main()
