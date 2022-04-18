import sys
#sys.stdin = open("input.txt", "r")

def printStaff(song):
    staff = {'G':[], 'F':[], 'E':[], 'D':[], 'C':[], 'B':[], 'A':[], 'g':[], 'f':[], 'e':[], 'd':[], 'c':[], 'b':[], 'a':[]}
    for note in song:
        staff[note[0]].append(note[1])
    for key in staff:
        print(key + ":", end="")
        for i in range(max(staff[key])):
            if i < len(staff[key]):
                print("*" * staff[key][i], end="")
            print(" ", end="")
        print()

def main():
    n = int(input())
    song = input().split()
    song = [list(note) for note in song]
    for note in song:
        if len(note) == 1:
            note.append(1)
        else:
            note[1] = int(note[1])
    printStaff(song)

if __name__ == '__main__':
    main()
