

from sys import stdin
from math import hypot

def main():
	line = stdin.readline().strip()
	gopher_x, gopher_y, dog_x, dog_y = [float(x) for x in line.split()] # read initial gopher and dog coordinates
	gopher_speed = hypot(gopher_x - dog_x, gopher_y - dog_y)
	dog_speed = gopher_speed * 2
	
	min_time = None
	min_hole = None
	for line in stdin:
		hole_x, hole_y = [float(x) for x in line.split()] # read hole coordinates
		gopher_time = hypot(gopher_x - hole_x, gopher_y - hole_y) / gopher_speed
		dog_time = hypot(dog_x - hole_x, dog_y - hole_y) / dog_speed
		
		if min_time is None or gopher_time < min_time:
			min_time = gopher_time
			min_hole = (hole_x, hole_y)
	
	if min_time is None or min_time >= dog_time:
		print("The gopher cannot escape")
	else:
		print("The gopher can escape through the hole at ({:.3f},{:.3f})".format(*min_hole))

if __name__ == '__main__':
	main()
