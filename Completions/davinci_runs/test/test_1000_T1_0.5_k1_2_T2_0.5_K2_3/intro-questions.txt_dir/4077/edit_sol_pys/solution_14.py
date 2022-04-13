
#median2
import sys
 
def median(lst):
	n = len(lst)
	if n < 1:
			return None
	if n % 2 == 1:
			return sorted(lst)[n//2]
	else:
			return sum(sorted(lst)[n//2-1:n//2+1])/2.0
 
def main():
	n, m = [int(x) for x in sys.stdin.readline().split()]
	lst = [int(x) for x in sys.stdin.readline().split()]
	print(lst)
	
if __name__ == '__main__':
	main() 
