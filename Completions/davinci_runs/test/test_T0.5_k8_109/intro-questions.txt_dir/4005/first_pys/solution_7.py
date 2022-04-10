

def main():
	w_corner_x, w_corner_y, w_width, w_height = map(int, input().split())
	b_corner_x, b_corner_y, b_width, b_height = map(int, input().split())
	b2_corner_x, b2_corner_y, b2_width, b2_height = map(int, input().split())

	if b_corner_x < w_corner_x and b_corner_x + b_width > w_corner_x + w_width and b_corner_y < w_corner_y and b_corner_y + b_height > w_corner_y + w_height:
		if b2_corner_x < w_corner_x and b2_corner_x + b2_width > w_corner_x + w_width and b2_corner_y < w_corner_y and b2_corner_y + b2_height > w_corner_y + w_height:
			print("NO")
		else:
			print("YES")
	else:
		print("YES")

if __name__ == '__main__':
	main()