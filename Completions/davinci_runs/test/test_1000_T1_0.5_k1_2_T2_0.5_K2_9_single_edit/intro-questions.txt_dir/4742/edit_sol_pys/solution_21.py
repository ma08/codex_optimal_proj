

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()  # list of notes
    n = int(input().strip())
    m1 = input().strip().split()  # list of notes of melody 1
    m2 = input().strip().split()  # list of notes of melody 2
    if m1 == m2:  # check if it's nonsense
        print("Nonsense")
    elif m1 == m2[::-1]:  # check if it's retrograde
        print("Retrograde")
    elif m2 == m1[::-1]:  # check if it's retrograde
        print("Retrograde")
    else:  # check if it's transposition or inversion
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:  # check if it's transposition
                print("Transposition")
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:  # check if it's inversion
                print("Inversion")
                break
        else:
            print("Nonsense")

if __name__ == "__main__":
    main()
