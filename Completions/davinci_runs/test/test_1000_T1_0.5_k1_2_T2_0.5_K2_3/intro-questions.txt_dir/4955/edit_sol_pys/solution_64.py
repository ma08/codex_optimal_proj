
#Program starts here.
import sys

#Reading in input.
n = int(sys.stdin.readline().strip()) #the number of notes
notes = sys.stdin.readline().strip().split() #the notes

#Initializing variables.
notes_dict = {'A':0, 'A#':1, 'B':2, 'C':3, 'C#':4, 'D':5, 'D#':6, 'E':7, 'F':8, 'F#':9, 'G':10, 'G#':11}
notes_list = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']

#Finding the scale.
if notes[0] in notes_dict:
    starting_note = notes_dict[notes[0]]
else:
    starting_note = notes_dict[notes[0][0] + '#']

scale_dict = {}

for i in range(0, 12):
    scale_dict[i] = [0] * 12

for i in range(0, 12):
    scale_dict[i][i] = 1

    if i + 2 <= 11:
        scale_dict[i][i + 2] = 1
    elif i + 2 > 11:
        scale_dict[i][i + 2 - 12] = 1

    if i + 4 <= 11:
        scale_dict[i][i + 4] = 1
    elif i + 4 > 11:
        scale_dict[i][i + 4 - 12] = 1

    if i + 5 <= 11:
        scale_dict[i][i + 5] = 1
    elif i + 5 > 11:
        scale_dict[i][i + 5 - 12] = 1

    if i + 7 <= 11:
        scale_dict[i][i + 7] = 1
    elif i + 7 > 11:
        scale_dict[i][i + 7 - 12] = 1

    if i + 9 <= 11:
        scale_dict[i][i + 9] = 1
    elif i + 9 > 11:
        scale_dict[i][i + 9 - 12] = 1

    if i + 11 <= 11:
        scale_dict[i][i + 11] = 1
    elif i + 11 > 11:
        scale_dict[i][i + 11 - 12] = 1

#Checking if the notes fit in the scale.
fits = False

for i in range(0, 12):
    if scale_dict[i][starting_note] == 1:
        fits = True
        for j in range(0, n):
            if notes[j] in notes_dict:
                if scale_dict[i][notes_dict[notes[j]]] == 0:
                    fits = False
            elif notes[j][0] + '#' in notes_dict:
                if scale_dict[i][notes_dict[notes[j][0] + '#']] == 0:
                    fits = False
        if fits == True:
            print(notes_list[i], end=' ')

if fits == False:
    print('None')
