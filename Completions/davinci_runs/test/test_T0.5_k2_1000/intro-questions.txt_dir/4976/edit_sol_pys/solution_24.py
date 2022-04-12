

from sys import stdin
from math import hypot

def main():
	line = stdin.readline().strip()
	goat_x, goat_y, dog_x, dog_y = [float(x) for x in line.split()]
	goat_speed = hypot(goat_x - dog_x, goat_y - dog_y)
	dog_speed = goat_speed * 2
	
	min_time = None
	min_hole = None
	for line in stdin:
		hole_x, hole_y = [float(x) for x in line.split()]
		goat_time = hypot(goat_x - hole_x, goat_y - hole_y) / goat_speed
		dog_time = hypot(dog_x - hole_x, dog_y - hole_y) / dog_speed
		
		if min_time is None or goat_time < min_time or (goat_time == min_time and hypot(goat_x - hole_x, goat_y - hole_y) < hypot(goat_x - min_hole[0], goat_y - min_hole[1])):
			min_time = goat_time
			min_hole = (hole_x, hole_y)
	
	if min_time is None or min_time >= dog_time:
		print("The goat cannot escape.")
	else:
		print("The gopher can escape through the hole at ({:.3f},{:.3f}).".format(*min_hole))

if __name__ == '__main__':
	main()
