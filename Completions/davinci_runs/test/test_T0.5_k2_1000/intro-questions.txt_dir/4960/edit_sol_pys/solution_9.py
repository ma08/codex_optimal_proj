

#-----main-----#
def main():
	binNum = input() #get input
	num = len(binNum) #get length of input
	if num % 3 == 1:
		binNum = "00" + binNum #add two 0s to the front
	elif num % 3 == 2:
		binNum = "0" + binNum
	octNum = ""
	for i in range(0, num, 3):
		octNum += str(int(binNum[i:i+3], 2))
	print(octNum)

main()
