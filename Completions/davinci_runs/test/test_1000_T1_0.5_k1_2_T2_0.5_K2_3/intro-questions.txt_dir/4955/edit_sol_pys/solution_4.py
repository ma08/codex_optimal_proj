
import sys

def get_notes_from_note(note):
    return [note, note + '#', note + '##']

def get_notes_from_scale(scale):
    note = scale[0]
    notes = [note]
    for interval in scale[1:]:
        if interval == '2':
            note = get_notes_from_note(note)[1] # half-tone
        else:
            note = get_notes_from_note(note)[2] # whole-tone
        notes.append(note)
    return notes

def get_scales():
    scales = []
    notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
    intervals = ['2212221', '2122212', '2221221', '2212212', '1222221', '2122221', '2212122']
    for note in notes:
        for interval in intervals:
            scales.append(note + ' ' + interval)
    return scales

def get_notes_from_song(song):
    return song.split(' ')

def is_scale(scale, song):
    notes = get_notes_from_scale(scale)
    for i in range(len(song)):
        if song[i] not in notes:
            return False
    return True

def get_song_scales(song):
    scales = get_scales()
    song_scales = []
    for scale in scales:
        scale = scale.split(' ') # ['C', '2212221']
        if is_scale(scale[1], song): # [2212221, 'E C D E F G A B C']
            song_scales.append(scale[0]) # ['C']
    return song_scales

def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline().rstrip()
    song = get_notes_from_song(song)
    song_scales = get_song_scales(song)
    if song_scales:
        print(' '.join(song_scales))
    else:
        print('none')

if __name__ == '__main__':
    main()
