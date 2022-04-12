#!/usr/bin/env python3

import sys

def main():
    note_map = {
        'A': 'a',
        'B': 'b',
        'C': 'c',
        'D': 'd',
        'E': 'e',
        'F': 'f',
        'G': 'g'
    }
    num_notes = int(sys.stdin.readline().strip())
    notes = sys.stdin.readline().strip().split()
    notes = [note.upper() for note in notes]
    notes = [note.replace('2', '*') for note in notes]  # whole note
    notes = [note.replace('3', '**') for note in notes]  # half note
    notes = [note.replace('4', '***') for note in notes]  # quarter note
    notes = [note.replace('5', '****') for note in notes]  # eighth note
    notes = [note.replace('6', '*****') for note in notes]  # sixteenth note
    notes = [note.replace('7', '******') for note in notes]  # thirty-second note
    notes = [note.replace('8', '*******') for note in notes]  # sixty-fourth note
    notes = [note.replace('9', '********') for note in notes]  # one-hundred-twenty-eighth note
    
    staff = {
        'G': [],
        'F': [],
        'E': [],
        'D': [],
        'C': [],
        'B': [],
        'A': [],
        'g': [],
        'f': [],
        'e': [],
        'd': [],
        'c': [],
        'b': [],
        'a': []
    }
    
    for note in notes:
        if len(note) == 1:
            note += '*'
        if note[0] in note_map:
            staff[note_map[note[0]]].append(note[1:])
        else:
            staff[note[0]].append(note[1:])
            
    for key in staff:
        print(key + ':', end='')
        for i in range(len(staff[key])):
            if i == 0:
                print(' ' * (42 - len(staff[key][i])), end='')
            else:
                print(' ' * (44 - len(staff[key][i])), end='')
            print(staff[key][i], end='')
        print()


main()
