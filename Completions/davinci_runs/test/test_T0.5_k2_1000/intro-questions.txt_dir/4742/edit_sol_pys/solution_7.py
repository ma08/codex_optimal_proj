

def main():
    notes = "C C# D D# E F F# G G# A A# B".split()
    n = int(input().strip())
    m1 = input().strip().split()
    m2 = input().strip().split()
    if m1 == m2:
        print("SAME")
    elif m1 == m2[::-1]:
        print("INVERSION")
    elif m2 == m1[::-1]:
        print("RETROGRADE")
    else:
        for i in range(len(m1)):
            if m2[i] == notes[(notes.index(m1[i]) + n) % 12]:
                print("TRANSPOSITION")
                break
            if m2[i] == notes[(notes.index(m1[0]) - (notes.index(m1[i]) - notes.index(m1[0]))) % 12]:
                print("INVERSION")
                break
        else:
            print("NONSENSE")

if __name__ == "__main__":
    main()
