
import sys

def get_notes(note):
    return [note, note + "#", note + "##"]

def get_notes_from_scale(scale):
    notes = []
    for note in scale:
        if note == "2":
            notes.append(get_notes(notes[-1])[1])
        else:
            notes.append(get_notes(notes[-1])[2])
    return notes

def get_scales():
    scales = []
    for note in ["A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#"]:
        for scale in ["2212221", "2122212", "2221221", "2212212", "1222221", "2122221", "2221212"]:
            scales.append(note + " " + scale)
    return scales

def get_song(song):
    song = song.split(" ")
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
        scale = scale.split(" ")
        if is_scale(scale[1], song):
            song_scales.append(scale[0])
    return song_scales

def main():
    n = int(sys.stdin.readline())
    song = sys.stdin.readline()
    song = get_song(song)
    song_scales = get_song_scales(song)
    if song_scales:
        print(" ".join(song_scales))
    else:
        print("none")

if __name__ == "__main__":
    main()
