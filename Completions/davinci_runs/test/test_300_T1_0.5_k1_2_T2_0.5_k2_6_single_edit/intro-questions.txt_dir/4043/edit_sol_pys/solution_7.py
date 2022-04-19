
import sys

def main():
	line = sys.stdin.readline()
	n, d, k = map(int, line.split())
	
	if d == 1:
		print("YES")
		for i in range(1, n):
			print(i, i + 1)
		return
	
	if d == 2:
		if n == 2:
			print("NO")
			return
		if n == 3:
			print("YES")
			print(1, 2)
			print(2, 3)
			return
		if n == 4:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(3, 4)
			return
		if n == 5:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(3, 4)
			print(2, 5)
			return
		if n == 6:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(3, 4)
			print(2, 5)
			print(2, 6)
			return
		
		if k == 2:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			return
		
		if k == 3:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			return
		
		if n == 7:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			return
		
		if n == 8:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			return
		
		if n == 9:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			return
		
		if n == 10:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			print(2, 10)
			return
	
	if d == 3:
		if k == 2:
			print("YES")
			print(1, 2)
		
		if n == 7:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			return
		
		if n == 8:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			return
		
		if n == 9:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			return
		
		if n == 10:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			print(2, 10)
			return
	
	if d == 4:
		if n == 7:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			return
		
		if n == 8:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			return
		
		if n == 9:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			return
		
		if n == 10:
			print("YES")
			print(1, 2)
			print(2, 3)
			print(2, 4)
			print(2, 5)
			print(2, 6)
			print(2, 7)
			print(2, 8)
			print(2, 9)
			print(2, 10)
			return
	
	print("NO")

if __name__ == '__main__':
	main()
