

#-----Solution-----

#Get input
num = int(input())
cheeses = []
for i in range(num):
	cheeses.append(input().split())

#Count soft and hard cheeses
soft = []
hard = []
for cheese in cheeses:
	if cheese[1] == "soft":
		soft.append(cheese[0])
	elif cheese[1] == "hard":
		hard.append(cheese[0])

#Output
print(len(hard))