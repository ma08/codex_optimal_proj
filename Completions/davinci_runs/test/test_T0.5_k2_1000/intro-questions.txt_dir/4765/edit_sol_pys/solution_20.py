
import sys

def main():
	meal = []
	for line in sys.stdin:
		meal.append([int(x) for x in line.split()])
	meal.pop(0)

	# print(meal)
	
	# min_dif = 1000000000
	# for i in range(len(meal)):
	# 	for j in range(i+1, len(meal)):
	# 		s = meal[i][0]*meal[j][0] # sugar
	# 		b = meal[i][1]+meal[j][1] # bitter
	# 		dif = abs(s-b) # difference
	# 		if dif < min_dif:
	# 			min_dif = dif
	# print(min_dif)
	
	# min_dif = 1000000000
	# for i in range(len(meal)):
	# 	for j in range(i+1, len(meal)):
	# 		for k in range(j+1, len(meal)):
	# 			s = meal[i][0]*meal[j][0]*meal[k][0] # sugar
	# 			b = meal[i][1]+meal[j][1]+meal[k][1] # bitter
	# 			dif = abs(s-b) # difference
	# 			if dif < min_dif:
	# 				min_dif = dif
	# print(min_dif)
	
	min_dif = 1000000000
	for i in range(len(meal)):
		for j in range(i+1, len(meal)):
			for k in range(j+1, len(meal)):
				for l in range(k+1, len(meal)):
					s = meal[i][0]*meal[j][0]*meal[k][0]*meal[l][0] # sugar
					b = meal[i][1]+meal[j][1]+meal[k][1]+meal[l][1] # bitter
					dif = abs(s-b) # difference
					if dif < min_dif:
						min_dif = dif
	print(min_dif)

if __name__ == '__main__':
	main()
