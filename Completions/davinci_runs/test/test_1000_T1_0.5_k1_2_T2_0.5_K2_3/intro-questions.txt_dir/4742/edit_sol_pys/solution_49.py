

import sys

def main():
    # Read the input
    l = int(sys.stdin.readline())
    melody1 = sys.stdin.readline().split()
    melody2 = sys.stdin.readline().split()

    # Check if transposition (transpose each note up by one semitone) 
    if melody2 == [transpose(note) for note in melody1]:
        print("Transposition")
    # Check if retrograde (reverse the melody)
    elif melody2 == melody1[::-1]:
        print("Retrograde")
    # Check if inversion (invert each note around the first note)
    elif melody2 == [invert(note, melody1[0]) for note in melody1]:
        print("Inversion")
    # Else, it's nonsense
    else:
        print("Nonsense")

def transpose(note):
    """
    Transpose a note up by one semitone.
    """
    # Create a list of all the notes in order
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    # Find the index of the current note
    index = notes.index(note)
    # If the note is the last note in the list, transpose it to the first note
    if index == len(notes) - 1:
        transposed_note = notes[0]
    # Else, transpose it to the next note
    else:
        transposed_note = notes[index + 1]

    return transposed_note

def invert(note, first_note):
    """
    Invert a note around the first note.
    """
    # Create a list of all the notes in order
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    # Find the index of the current note
    index = notes.index(note)
    # Find the index of the first note
    first_index = notes.index(first_note)
    # Find the difference between the two notes
    difference = index - first_index
    # If the difference is positive, invert it to the negative difference
    if difference > 0:
        difference = -difference
    # If the difference is negative, invert it to the positive difference
    elif difference < 0:
        difference = -difference
    # If the difference is zero, the note is the same as the first
    else:
        return first_note
    # Find the index of the inverted note
    inverted_index = first_index + difference
    # If the inverted note is outside the range of the list, wrap it around to the other end
    if inverted_index < 0:
        inverted_index = len(notes) - abs(inverted_index)
    elif inverted_index > len(notes) - 1:
        inverted_index = abs(len(notes) - inverted_index)
    # Find the inverted note
    inverted_note = notes[inverted_index]

    return inverted_note

# Call the main function
if __name__ == "__main__":
    main()
