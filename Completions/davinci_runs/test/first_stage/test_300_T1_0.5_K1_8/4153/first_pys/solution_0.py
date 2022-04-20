

N = int(input())
S = input()

bottom_red_count = 0
top_blue_count = 0

for i in range(N):
	if S[i] == '0':
		bottom_red_count += 1
	else:
		top_blue_count += 1
	if bottom_red_count == top_blue_count:
		print(bottom_red_count + top_blue_count)
		break