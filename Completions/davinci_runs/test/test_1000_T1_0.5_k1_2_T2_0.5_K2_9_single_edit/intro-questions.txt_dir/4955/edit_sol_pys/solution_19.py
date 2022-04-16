

def get_possible_scales(song):
	"""
	>>> get_possible_scales(['C', 'D', 'F', 'D', 'C', 'D', 'F', 'F', 'F', 'C'])
	['A#', 'C', 'D#', 'F']
	"""
	def get_scale(note):
		scale = [note]
		while len(scale) < 8:
			if len(scale) == 3 or len(scale) == 7:
				scale.append(notes[notes.index(scale[-1]) + 1])
			else:
				scale.append(notes[notes.index(scale[-1]) + 2])
		return scale

	notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	scales = []
	for note in notes:
		scale = get_scale(note)
		if all(song_note in scale for song_note in song):
			scales.append(note[0])
	if len(scales) == 0:
		print 'none'
	else:
		print ' '.join(scales)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
