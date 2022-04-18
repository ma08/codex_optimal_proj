

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()
    n = int(input().strip())  # number of notes
    m1 = input().strip().split()  # first melody
    m2 = input().strip().split()  # second melody
    if m1 == m2:
        print("Nonsense")
    elif m1[::-1] == m2:
        print("Retrograde")
    elif m2[::-1] == m1:
        print("Retrograde")
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:
                print("Transposition")
                break
            if m2[i] == notes[(notes.index(m1[0]) -
                               (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
