

import sys

def main():
	meal = []
	for line in sys.stdin:
		meal.append([int(x) for x in line.split()])
	meal.pop(0)

	# print(meal)

	# min_diff = 1000000000
	# for i in range(len(meal)):
	# 	for j in range(i+1, len(meal)):
	# 		s = meal[i][0]*meal[j][0]
	# 		b = meal[i][1]+meal[j][1]
	# 		diff = abs(s-b)
	# 		if diff < min_diff:
	# 			min_diff = diff
	# print(min_diff)

	# min_diff = 1000000000
	# for i in range(len(meal)):
	# 	for j in range(i+1, len(meal)):
	# 		for k in range(j+1, len(meal)):
	# 			s = meal[i][0]*meal[j][0]*meal[k][0]
	# 			b = meal[i][1]+meal[j][1]+meal[k][1]
	# 			diff = abs(s-b)
	# 			if diff < min_diff:
	# 				min_diff = diff
	# print(min_diff)

	min_diff = 1000000000
	for i in range(len(meal)):
		for j in range(i+1, len(meal)):
			for k in range(j+1, len(meal)):
				for l in range(k+1, len(meal)):
					s = meal[i][0]*meal[j][0]*meal[k][0]*meal[l][0]
					b = meal[i][1]+meal[j][1]+meal[k][1]+meal[l][1]
					diff = abs(s-b)
					if diff < min_diff:
						min_diff = diff
	print(min_diff)

if __name__ == '__main__':
	main()
