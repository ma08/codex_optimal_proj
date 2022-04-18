

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def main():
    length = int(input())
    melody1 = [int(x) for x in input().split()]
    melody2 = [int(x) for x in input().split()]

    # Transposition
    if melody1 == melody2:
        print("Nonsense")
        return
    transposed = True
    for i in range(length):
        if melody1[i] != melody2[(i+1)%length]:
            transposed = False
            break
    if transposed:
        print("Transposition")
        return

    # Retrograde
    retrograde = True
    for i in range(length):
        if melody1[i] != melody2[length-i-1]:
            retrograde = False
            break
    if retrograde:
        print("Retrograde")
        return

    # Inversion
    inversion = True
    for i in range(length):
        if i == 0:
            continue
        if melody1[i] != notes.index(melody2[i]) + notes.index(melody2[0]):
            inversion = False
            break
    if inversion:
        print("Inversion")
        return

    print("Nonsense")

if __name__ == "__main__":
    main()
