
import sys

def get_notes_from_note(note):
    return [note, note + '#', note + '##']

def get_notes_from_scale(scale):
    notes = []
    for i in range(0, len(scale)):
        notes += get_notes_from_note(scale[i])
    return notes

def get_scales():
    scales = []
    for note in ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']:
        for scale in ['2212221', '2122212', '2221221', '2212212', '1222221', '2122221', '2212122', '1222122']:
            scales.append(note + ' ' + scale)
    return scales

def get_notes_from_song(song):
    return song.split(' ')

def is_scale(scale, song):
    notes = get_notes_from_scale(scale)
    for note in song:
        if note not in notes and note != '\n':
            return False
    return True

def get_song_scales(song):
    scales = get_scales()
    song_scales = []
    for scale in scales:
        scale = scale.split(' ')[1]
        if is_scale(scale, song):
            song_scales.append(scale)
    return song_scales

def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline()
    song = get_notes_from_song(song)
    song_scales = get_song_scales(song)
    if song_scales:
        print(' '.join(song_scales))
    else:
        print('none')

if __name__ == '__main__':
    main()
