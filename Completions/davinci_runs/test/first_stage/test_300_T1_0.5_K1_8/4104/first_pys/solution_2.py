

#Solution

def sol(inp):
	lst = list(map(int,inp.split('+')))
	return sum(lst)

print(sol(input()))