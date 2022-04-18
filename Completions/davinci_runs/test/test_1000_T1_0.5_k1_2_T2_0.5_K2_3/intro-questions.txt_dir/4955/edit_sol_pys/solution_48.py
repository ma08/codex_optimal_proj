
import sys

def get_notes_from_note(note):
    return note, note + '#', note + '##'

def get_notes_from_scale(scale):
    notes = []
    for note in scale:
        if note == '2':
            notes.append(get_notes_from_note(notes[-1])[1])
        elif note == '1':
            notes.append(get_notes_from_note(notes[-1])[2])
    return notes

def get_scales():
    scales = []
    for scale in ['2212221', '2122212', '2221221', '2212212', '1222221', '2122221', '2212122']:
        scales.append(get_notes_from_scale(scale))
    return scales

def get_song(song):
    song = song.split()
    return song

def is_scale(scale, song):
    return set(scale).issubset(set(song))

def get_song_scales(song):
    scales = get_scales()
    return [scale[0] for scale in scales if is_scale(scale, song)]

def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline().rstrip()
    song = get_song(song)
    song_scales = get_song_scales(song)
    if song_scales:
        print(' '.join(sorted(song_scales)))
    else:
        print('none')

if __name__ == '__main__':
    main()
