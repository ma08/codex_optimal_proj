
import math

def main():
	sides = list(map(int, input().split()))
	sides.sort()
	s1, s2, s3, s4 = sides

	# Heron's formula
	s = (s1 + s2 + s3 + s4) / 2
	area = math.sqrt((s - s1) * (s - s2) * (s - s3) * (s - s4))

	print(area)

if __name__ == '__main__':
	main()
