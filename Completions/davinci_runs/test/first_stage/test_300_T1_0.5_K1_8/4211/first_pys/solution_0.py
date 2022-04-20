

from sys import stdin

def main():
	N = int(stdin.readline())
	B = [int(x) for x in stdin.readline().split()]
	
	A = [0] * N
	
	A[0] = B[0]
	A[N-1] = B[N-2]
	
	for i in range(1, N-1):
		A[i] = max(B[i-1], B[i])
		
	print(sum(A))
	
if __name__ == "__main__":
	main()