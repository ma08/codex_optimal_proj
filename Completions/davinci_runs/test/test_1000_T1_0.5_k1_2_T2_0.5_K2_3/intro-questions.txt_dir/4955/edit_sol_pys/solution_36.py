

import sys

def get_possible_scales(song):
	"""
	>>> get_possible_scales(['C', 'D', 'F', 'D', 'C', 'D', 'F', 'F', 'F', 'C'], 'C')
	['A#', 'C', 'D#', 'F', 'G']
	"""
	def get_scale(note):
		scale = [note]
		while len(scale) < 12:
			if len(scale) == 3 or len(scale) == 7:
				scale.append(notes[(notes.index(scale[-1]) + 1) % len(notes)])
			else:
				scale.append(notes[(notes.index(scale[-1]) + 2) % len(notes)])
		return scale

	notes = ['A', 'A#', 'B', 'C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#']
	scales = []
	for note in notes:
		scale = get_scale(note)
		if all(song_note in scale for song_note in song):
			scales.append(note + 'm' if note[-1] == '#' else note)
	if len(scales) == 0:
		print 'None'
	else:
		print ' '.join(sorted(scales))

if __name__ == '__main__':
	# import doctest
	# doctest.testmod()
	get_possible_scales(sys.argv[1].split(','), sys.argv[2])
