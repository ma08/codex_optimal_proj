

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()
    n = int(input().strip()) # number of notes
    m1 = input().strip().split() # first line of notes
    m2 = input().strip().split() # second line of notes
    if m1 == m2:
    # if the first line is the same as the second line in reverse
        print("Nonsense")
    elif m1 == m2[::-1]:
    # if the second line is the same as the first line in reverse
        print("Retrograde")
    elif m2 == m1[::-1]:
        print("Retrograde")
        # check for transposition
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:
                print("Transposition")
        # check for inversion
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
