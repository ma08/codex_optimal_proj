

def main():
	n = int(input())
	s = input()
	t = input()
	
	if s == t:
		print('0')
		return
	
	for i in range(n):
		if s[i] == t[i]:
			continue
		
		for j in range(i+1,n):
			if s[j] == t[i]:
				s = s[:i] + s[j] + s[i+1:j] + s[i] + s[j+1:]
				print(i+1,j+1)
				break


if __name__ == '__main__':
	main()