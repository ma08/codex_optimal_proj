

a = int(raw_input())

while True:
	if sum(int(d) for d in str(a))%4 == 0:
		break
	else:
		a += 1

print a