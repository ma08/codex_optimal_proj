

def is_transposition(m1, m2, n):
    # m1 is a transposition of m2 if m2 can be obtained by shifting m1 by some number of semitones.
    # A transposition is only possible if the number of notes in m1 and m2 are the same
    if n != len(m1) or n != len(m2):
        return False
    for i in range(n):
        if m1[i] != m2[(i + 1) % n]:
            return False
    return True

def is_retrograde(m1, m2, n):
    # m1 is a retrograde of m2 if m2 is the reverse of m1.
    if n != len(m1) or n != len(m2):
        return False
    for i in range(n):
        if m1[i] != m2[n - i - 1]:
            return False
    return True

def is_inversion(m1, m2, n):
    # m1 is an inversion of m2 if m2 can be obtained by inverting m1 about the first note in m1.
    # An inversion is only possible if the number of notes in m1 and m2 are the same
    if n != len(m1) or n != len(m2):
        return False
    for i in range(1, n):
        if m1[i] != m2[(i + 1) % n]:
            return False
    return True

def is_nonsense(m1, m2, n):
    return not (is_transposition(m1, m2, n) or is_retrograde(m1, m2, n) or is_inversion(m1, m2, n))

def main():
    # read the number of notes in each melody
    n = int(input())
    # read the first melody
    m1 = input().split()
    # read the second melody
    m2 = input().split()
    if is_transposition(m1, m2, n):
        print("Transposition")
    elif is_retrograde(m1, m2, n):
        print("Retrograde")
    elif is_inversion(m1, m2, n):
        print("Inversion")
    else:
        print("Nonsense")

if __name__ == "__main__":
    main()
