

contestants, huffle_puffs = map(int, input().split()) #(int, int)

if huffle_puffs <= contestants // 2:
	print("strict")
elif huffle_puffs <= contestants:
	print("not strict")
else:
	print("impossible")
