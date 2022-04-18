

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()  # chromatic scale
    n = int(input().strip())
    m1 = input().strip().split()  # original melody
    m2 = input().strip().split()  # transformed melody
    if m1 == m2:
        print("Nonsense")
    elif m1 == m2[::-1] or m2 == m1[::-1]:  # if one is the reverse of the other
        print("Retrograde")
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:  # transposition
                print("Transposition")
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:  # inversion
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
