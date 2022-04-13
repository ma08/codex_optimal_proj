
import sys

def get_notes_from_note(note):
    return [note, note + '#', note + '##']

def get_notes_from_scale(scale):
    note = scale[0]
    notes = [note]
    for i in range(1, len(scale)):
        if scale[i] == '2':
            note = get_notes_from_note(note)[1]
        else:
            note = get_notes_from_note(note)[2]
        notes.append(note)
    return notes

def get_scales():
    scales = []
    for note in get_notes_from_note('A'):
        for scale in ['2212221', '2122212', '2221221', '2212212', '1222221', '2122221', '2212122']:
            scales.append(note + ' ' + scale)
    return scales

def get_song(song):
    song = song.split(' ')
    return song

def is_scale(scale, song):
    notes = get_notes_from_scale(scale)
    for note in song:
        if note not in notes:
            return False
    return True

def get_song_scales(song):
    scales = get_scales()
    song_scales = []
    for scale in scales:
        scale = scale.split(' ')
        if is_scale(scale[1], song):
            song_scales.append(scale[0])
    return song_scales

def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline()
    song = get_song(song)
    song_scales = get_song_scales(song)
    if song_scales:
        print(' '.join(song_scales))
    else:
        print('none')

if __name__ == '__main__':
    main()
