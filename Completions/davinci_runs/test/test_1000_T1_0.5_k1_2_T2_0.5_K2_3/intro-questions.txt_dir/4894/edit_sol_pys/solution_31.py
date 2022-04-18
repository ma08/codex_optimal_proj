# input

n = int(input())
notes = input().split()
# staff

staff = {'C': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'D': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'E': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'F': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'G': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'A': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:'],
         'B': ['G:', 'F:', 'E:', 'D:', 'C:', 'B:', 'A:', 'g:', 'f:', 'e:', 'd:', 'c:', 'b:', 'a:']}

# write in the staff
for i in range(len(notes)):
    note = notes[i]
    duration = 1
    if len(note) == 2:
        duration = int(note[1])
    if note[0] == 'C' or note[0] == 'c':
        staff['C'][12] += '*' * duration + ' '
    elif note[0] == 'D' or note[0] == 'd':
        staff['D'][11] += '*' * duration + ' '
    elif note[0] == 'E' or note[0] == 'e':
        staff['E'][10] += '*' * duration + ' '
    elif note[0] == 'F' or note[0] == 'f':
        staff['F'][9] += '*' * duration + ' '
    elif note[0] == 'G' or note[0] == 'g':
        staff['G'][8] += '*' * duration + ' '
    elif note[0] == 'A' or note[0] == 'a':
        staff['A'][7] += '*' * duration + ' '
    elif note[0] == 'B' or note[0] == 'b':
        staff['B'][6] += '*' * duration + ' '

# print the staff
for i in range(len(staff['C'])):
    print(staff['C'][i])
