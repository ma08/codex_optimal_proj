

notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B', 'C']

def transposition(melody1, melody2):
    for i in range(len(melody1)):
        if melody1[i] != melody2[i]:
            return False
    return True

def retrograde(melody1, melody2):
    if melody1 == melody2[::-1]:
        return True
    else:
        return False

def inversion(melody1, melody2):
    for i in range(len(melody1)):
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
