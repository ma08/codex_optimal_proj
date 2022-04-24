
import sys

def main():
	n = int(sys.stdin.readline().strip())
	points = []
	for i in range(n):
		x, y, h = map(int, sys.stdin.readline().strip().split())
		points.append((x, y, h))
	# print(points)
	center_x = 0
	center_y = 0
	height = 0
	for i in range(n):
		for j in range(i + 1, n):
			x1, y1, h1 = points[i]
			x2, y2, h2 = points[j]
			if x1 == x2:
				center_x = x1
				center_y = (y1 + y2) // 2
				height = h1 + abs(y1 - center_y)
			elif y1 == y2:
				center_x = (x1 + x2) // 2
				center_y = y1
				height = h1 + abs(x1 - center_x)
			else:
				center_x = (x1 + x2) // 2
				center_y = (y1 + y2) // 2
				height = h1 + abs(x1 - center_x) + abs(y1 - center_y)
			# print(center_x, center_y, height)
			if all(h == height - abs(x - center_x) - abs(y - center_y) for x, y, h in points):
				print(center_x, center_y, height)
				break

if __name__ == "__main__":
	main()
