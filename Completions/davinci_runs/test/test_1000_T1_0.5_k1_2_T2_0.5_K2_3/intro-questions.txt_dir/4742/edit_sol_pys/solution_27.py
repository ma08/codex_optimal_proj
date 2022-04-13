

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']

def transposition(melody1, melody2):
    if melody1[0] == melody2[0] or (melody1[0] == 'C' and melody2[0] == 'H') or (melody1[0] == 'H' and melody2[0] == 'C'):
        return True
    else:
        return False

def retrograde(melody1, melody2):
    if melody1 == melody2[::-1] and melody1[0] == melody2[0]:
        return True
    else:
        return False

def inversion(melody1, melody2):
    for i in range(0, len(melody1)):
        if notes.index(melody1[i]) + notes.index(melody2[i]) != 11:
            return False
    return True

def main():
    l = int(input())
    melody1 = input().split()
    melody2 = input().split()
    if transposition(melody1, melody2):
        print('Transposition')
    elif retrograde(melody1, melody2):
        print('Retrograde')
    elif inversion(melody1, melody2):
        print('Inversion')
    else:
        print('Nonsense')

if __name__ == '__main__':
    main()
