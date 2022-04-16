
n = int(input())
notes = input().split()

staff = {'C': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'D': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'E': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'F': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'G': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'A': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'B': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:']}

for i in range(len(notes)):
    note = notes[i]
    duration = 1
    if len(note) == 2:
        duration = int(note[1])
    if note[0] == 'C':
        staff['C'][12] += '*' * duration + '_'
    elif note[0] == 'D':
        staff['D'][11] += '*' * duration + '_'
    elif note[0] == 'E':
        staff['E'][10] += '*' * duration + '_'
    elif note[0] == 'F':
        staff['F'][9] += '*' * duration + '_'
    elif note[0] == 'G':
        staff['G'][8] += '*' * duration + '_'
    elif note[0] == 'A':
        staff['A'][7] += '*' * duration + '_'
    elif note[0] == 'B':
        staff['B'][6] += '*' * duration + '_'
    elif note[0] == 'c':
        staff['C'][5] += '*' * duration + '_'
    elif note[0] == 'd':
        staff['D'][4] += '*' * duration + '_'
    elif note[0] == 'e':
        staff['E'][3] += '*' * duration + '_'
    elif note[0] == 'f':
        staff['F'][2] += '*' * duration + '_'
    elif note[0] == 'g':
        staff['G'][1] += '*' * duration + '_'
    elif note[0] == 'a':
        staff['A'][0] += '*' * duration + '_'
    elif note[0] == 'b':
        staff['B'][-1] += '*' * duration + '_'

for i in range(len(staff['C'])):
    print(staff['C'][i])
