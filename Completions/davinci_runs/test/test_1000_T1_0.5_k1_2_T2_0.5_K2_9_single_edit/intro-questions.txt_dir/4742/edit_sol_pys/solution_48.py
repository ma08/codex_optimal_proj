
    
notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

def transposition(melody1, melody2):
    return melody1[0] == melody2[0] or (melody1[0] == 'C' and melody2[0] == 'B') or (melody1[0] == 'B' and melody2[0] == 'C')

def retrograde(melody1, melody2):
    return melody1 == melody2[::-1]

def inversion(melody1, melody2):
    return melody1[0] == melody2[0] and all(notes.index(melody1[i]) + notes.index(melody2[i]) == 11 for i in range(1, len(melody1)))

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
