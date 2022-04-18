
import sys

def main():
    n = int(sys.stdin.readline().strip()) #number of lines
    notes = sys.stdin.readline().strip().split() #notes
    staff = {'G':'', 'F':'', 'E':'', 'D':'', 'C':'', 'B':'', 'A':'', 'g':'', 'f':'', 'e':'', 'd':'', 'c':'', 'b':'', 'a':''} #staff
    for note in notes: #loop through notes
        if len(note) == 1: #if the note is one character
            staff[note] += '*' #add a star to the staff
        else: #otherwise it is two characters
            staff[note[0]] += '*'*int(note[1]) #add the number of stars based on the second character
    for l in ['G', 'F', 'E', 'D', 'C', 'B', 'A', 'g', 'f', 'e', 'd', 'c', 'b', 'a']: #loop through each line of staff
        print(l+': '+staff[l]) #print the line of staff

main()
