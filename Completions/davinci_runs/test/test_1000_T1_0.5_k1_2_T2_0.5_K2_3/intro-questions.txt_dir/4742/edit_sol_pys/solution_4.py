

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()  # make list of notes
    n = int(input().strip())
    m1 = input().strip().split()
    # check if m1 == m2
    m2 = input().strip().split()
    if m1 == m2:
        print("Nonsense")
    elif m1 == m2[::-1]:
        print("Retrograde")
    elif m2 == m1[::-1]:
        print("Retrograde")
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:
                print("Transposition")
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0])) % 12]):
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
